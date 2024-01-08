package verifywebhook

import (
	"crypto/hmac"
	"crypto/sha512"
	"encoding/hex"
	"encoding/json"
	"errors"
	"io"

	"net/http"
	"strings"
)

// Hook is an inbound webhook
type Hook struct {
	Signature string

	Payload []byte
}

const signaturePrefix = "sha512=" ////set this to your signature prefix if any

func signBody(secret, body []byte) []byte {
	// Calculate HMAC
	computed := hmac.New(sha512.New, secret)
	computed.Write(body)
	return []byte(computed.Sum(nil))
}

func (h *Hook) SignedBy(secret []byte) bool {
	if !strings.HasPrefix(h.Signature, signaturePrefix) {
		return false
	}

	prefixLen := len(signaturePrefix)
	signature := h.Signature[prefixLen:]
	actualSignature := make([]byte, hex.DecodedLen(len(signature)))
	hex.Decode(actualSignature, []byte(signature))

	localSignature := signBody(secret, h.Payload)
	return hmac.Equal(localSignature, actualSignature)
}

func (h *Hook) Extract(dst interface{}) error {
	return json.Unmarshal(h.Payload, dst)
}

func New(req *http.Request) (hook *Hook, err error) {
	hook = new(Hook)
	if !strings.EqualFold(req.Method, "POST") {
		return nil, errors.New("Unknown method!")
	}

	// Extract signature
	if hook.Signature = req.Header.Get("X-Signature"); len(hook.Signature) == 0 {
		return nil, errors.New("No signature!")
	}

	// Get raw body
	hook.Payload, err = io.ReadAll(req.Body)
	return
}

func Parse(secret []byte, req *http.Request) (hook *Hook, err error) {
	hook, err = New(req)

	//Compare HMACs
	if err == nil && !hook.SignedBy(secret) {
		err = errors.New("Invalid signature")
	}
	return
}
