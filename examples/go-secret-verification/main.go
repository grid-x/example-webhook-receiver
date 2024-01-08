package main

import (
	"crypto/hmac"
	"crypto/sha512"
	"encoding/hex"
	"errors"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strings"
)

var webhookSecret string

func init() {
	webhookSecret = os.Getenv("WEBHOOK_SECRET")
	if webhookSecret == "" {
		log.Fatalf("webhook secret needs to be set in the WEBHOOK_SECRET environment variable")
	}
}

func handleVerification(w http.ResponseWriter, req *http.Request) {
	secretByte := []byte(webhookSecret)
	_, err := Parse(secretByte, req)
	if err != nil {
		log.Fatalf("webhook secret is incorrect: %v", err)
	}
}

func main() {

	http.HandleFunc("/gridx/events/appliance/online", handleVerification)

	http.ListenAndServe(":8080", nil)
}

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

	length := len(signaturePrefix)
	signaturePayload := []byte(h.Signature[length:])
	actual := make([]byte, hex.DecodedLen(len(signaturePayload)))
	hex.Decode(actual, signaturePayload)

	return hmac.Equal(signBody(secret, h.Payload), actual)
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
	hook.Payload, err = ioutil.ReadAll(req.Body)
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
