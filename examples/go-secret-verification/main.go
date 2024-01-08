package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/grid-x/webhook/examples/go-secret-verification/verifywebhook"
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
	_, err := verifywebhook.Parse(secretByte, req)
	if err != nil {
		log.Fatalf("webhook secret is incorrect: %v", err)
	}
	fmt.Printf("webhook secret is correct")
}

func main() {

	http.HandleFunc("/gridx/events/appliance/online", handleVerification)

	http.ListenAndServe(":8080", nil)
}
