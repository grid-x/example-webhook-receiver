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
)

type Error struct {
	Type     string `json:"type,omitempty"`
	Status   int32  `json:"status"`
	Title    string `json:"title"`
	Detail   string `json:"detail,omitempty"`
	Instance string `json:"instance,omitempty"`
}

type Verifier struct {
	secretKey string
}

func NewVerifier(secretKey string) *Verifier {
	return &Verifier{secretKey: secretKey}
}

func (v *Verifier) Verify(r *http.Request) error {
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

	calculatedDigest := calculateDigest(bodyBytes, v.secretKey)

	var match bool
	for _, received := range receivedDigests {
		if hmac.Equal(received, calculatedDigest) {
			match = true
			break
		}
	}

	if !match {
		return fmt.Errorf("no valid HMAC digest found")
	}

	return nil
}

// Middleware is an HTTP middleware that verifies the HMAC signature of a gridX webhook event's request body.
func (v *Verifier) Middleware(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if err := v.Verify(r); err != nil {
			slog.Warn("failed verifying HMAC signature", "error", err)
			w.WriteHeader(http.StatusUnauthorized)
			return
		}

		next.ServeHTTP(w, r)
	}
}

func parseSignatureHeader(signatureHeader string) ([][]byte, error) {
	digestsWithPrefixes := strings.Split(signatureHeader, ", ")
	if len(digestsWithPrefixes) == 0 {
		return [][]byte{}, errors.New("invalid signature header: found no digests")
	}

	digests := make([][]byte, 0, len(digestsWithPrefixes))
	for _, digestWithPrefix := range digestsWithPrefixes {
		if !strings.HasPrefix(digestWithPrefix, DigestPrefix) {
			return digests, errors.New("invalid signature header: found digest without prefix")
		}

		digestHex := strings.TrimPrefix(digestWithPrefix, DigestPrefix)

		digest, err := hex.DecodeString(digestHex)
		if err != nil {
			return digests, errors.New("invalid signature header: invalid digest")
		}

		digests = append(digests, digest)
	}

	return digests, nil
}

type Signer struct {
	secretKey string
}

func NewSigner(secretKey string) *Signer {
	return &Signer{secretKey: secretKey}
}

// Sign calculates a digest for the http.Request and adds it to the http.Request's SignatureHeader.
func (s *Signer) Sign(r *http.Request) error {
	bodyBytes, err := io.ReadAll(r.Body)
	if err != nil {
		return fmt.Errorf("failed to read body: %s", err)
	}
	r.Body = io.NopCloser(bytes.NewBuffer(bodyBytes))

	digestBytes := calculateDigest(bodyBytes, s.secretKey)

	r.Header.Set(SignatureHeader, DigestPrefix+hex.EncodeToString(digestBytes))

	return nil
}

func calculateDigest(bodyBytes []byte, secretKey string) []byte {
	mac := hmac.New(sha512.New, []byte(secretKey))
	mac.Write(bodyBytes)
	return mac.Sum(nil)
}
