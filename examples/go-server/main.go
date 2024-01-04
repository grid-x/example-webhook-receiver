/*
 * Webhook Event Receiver API
 *
 * This API describes the event webhook calling convention. In order to receive webhook events from the gridX API, third parties must implement endpoints according to this specification. In the following, the external partner API is referred to as  \"external API\", while the gridX API is called \"gridX\".
 *
 * API version: 1.0.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package main

import (
	"log"
	"net/http"

	openapi "github.com/GIT_USER_ID/GIT_REPO_ID/go"
)

func main() {
	log.Printf("Server started")

	WebhookReceiverAPIService := openapi.NewWebhookReceiverAPIService()
	WebhookReceiverAPIController := openapi.NewWebhookReceiverAPIController(WebhookReceiverAPIService)

	router := openapi.NewRouter(WebhookReceiverAPIController)

	log.Fatal(http.ListenAndServe(":8080", router))
}
