/*
 * Example XENON webhook receiver
 *
 * This is an example webhook receiver for XENON.
 *
 * API version: v1.0.0
 * Contact: developer-community@gridx.de
 */

package main

import (
	"log"
	"net/http"
	"os"

	openapi "github.com/grid-x/example-webhook-receiver/go"
	"github.com/grid-x/example-webhook-receiver/pkg/hmac"
)

func main() {
	log.Printf("Server started")

	DefaultAPIService := openapi.NewDefaultAPIService()
	DefaultAPIController := openapi.NewDefaultAPIController(DefaultAPIService)
	secretKey := os.Getenv("SECRET_KEY")
	if secretKey == "" {
		log.Fatal("SECRET_KEY environment variable not set")
	}
	requestVerifier := hmac.NewRequestVerifier(secretKey)

	router := openapi.NewRouter([]openapi.Router{DefaultAPIController}, requestVerifier)

	log.Fatal(http.ListenAndServe(":8080", router))
}
