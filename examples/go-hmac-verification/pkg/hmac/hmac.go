package hmac

import (
	"bytes"
	"crypto/hmac"
	"crypto/sha512"
	"encoding/hex"
	"errors"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"strings"
)

const (
	SignatureHeader = "X-Signature"
	DigestPrefix    = "sha512="
	DigestSeparator = ", "
)

func CalculateDigest(bytes []byte, secretKey string) []byte {
	mac := hmac.New(sha512.New, []byte(secretKey))
	mac.Write(bytes)
	return mac.Sum(nil)
}

type RequestVerifier struct {
	secretKey string
}

func NewRequestVerifier(secretKey string) *RequestVerifier {
	return &RequestVerifier{secretKey: secretKey}
}

// Middleware returns an http.HandlerFunc to be used as an HTTP middleware for verifying HMAC signatures of gridX
// webhook event requests.
func (v *RequestVerifier) Middleware(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if err := v.Verify(r); err != nil {
			slog.Warn("failed verifying HMAC signature", "error", err)
			w.WriteHeader(http.StatusUnauthorized)
			return
		}

		next.ServeHTTP(w, r)
	}
}

// Verify extracts all provided digests from an http.Request's SignatureHeader and verifies that at least of them has
// been calculated for exactly this http.Request with the secretKey provided through NewRequestVerifier.
func (v *RequestVerifier) Verify(r *http.Request) error {
	signatureHeader := r.Header.Get(SignatureHeader)
	if signatureHeader == "" {
		return fmt.Errorf("missing HMAC signature header")
	}

	receivedDigests, err := parseSignatureHeader(signatureHeader)
	if err != nil {
		return fmt.Errorf("invalid HMAC signature header")
	}

	bodyBytes, err := io.ReadAll(r.Body)
	if err != nil {
		return fmt.Errorf("failed to read body: %v", err)
	}
	// Restore the body so the next handler can read it.
	r.Body = io.NopCloser(bytes.NewBuffer(bodyBytes))

	calculated := CalculateDigest(bodyBytes, v.secretKey)

	var verified bool
	for _, received := range receivedDigests {
		if hmac.Equal(received, calculated) {
			verified = true
			break
		}
	}

	if !verified {
		return fmt.Errorf("no valid HMAC digest found")
	}

	return nil
}

func parseSignatureHeader(signatureHeader string) ([][]byte, error) {
	digestsWithPrefixes := strings.Split(signatureHeader, DigestSeparator)
	if len(digestsWithPrefixes) == 0 {
		return [][]byte{}, errors.New("found no digests")
	}

	digests := make([][]byte, 0, len(digestsWithPrefixes))
	for _, digestWithPrefix := range digestsWithPrefixes {
		if !strings.HasPrefix(digestWithPrefix, DigestPrefix) {
			return digests, errors.New("found digest without prefix")
		}
		digestHex := strings.TrimPrefix(digestWithPrefix, DigestPrefix)

		digest, err := hex.DecodeString(digestHex)
		if err != nil {
			return digests, errors.New("failed decoding digest")
		}

		digests = append(digests, digest)
	}

	return digests, nil
}

type RequestSigner struct {
	secretKeys []string
}

func NewRequestSigner(secretKeys []string) *RequestSigner {
	return &RequestSigner{secretKeys: secretKeys}
}

// Sign calculates a digest of the http.Request's body for each secretKey provided through NewRequestSigner.
// It then prefixes each of these digests with DigestPrefix, joins them together with DigestSeparator and sets the
// result on the http.Request's SignatureHeader.
func (s *RequestSigner) Sign(r *http.Request) error {
	bodyBytes, err := io.ReadAll(r.Body)
	if err != nil {
		return fmt.Errorf("failed to read body: %s", err)
	}
	r.Body = io.NopCloser(bytes.NewBuffer(bodyBytes))

	digests := make([]string, len(s.secretKeys))
	for i, secretKey := range s.secretKeys {
		digestBytes := CalculateDigest(bodyBytes, secretKey)
		digests[i] = DigestPrefix + hex.EncodeToString(digestBytes)
	}

	r.Header.Set(SignatureHeader, strings.Join(digests, DigestSeparator))

	return nil
}
