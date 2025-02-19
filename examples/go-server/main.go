/*
 * gridX Webhook Event Receiver API
 *
 * This API describes the event webhook calling convention. In order to receive webhook events from the gridX API, third parties must implement endpoints according to this specification. In the following, the external partner API is referred to as  \"external API\", while the gridX API is called \"gridX\".
 *
 * API version: 1.0.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"

	openapi "github.com/GIT_USER_ID/GIT_REPO_ID/go"
)

func (c CountStatusChange) Increment(id string, status string) {
	_, ok := c[id]
	if !ok {
		c[id] = StatusChange{}
	}

	statusChange := c[id]
	statusChange.counter = statusChange.counter + 1
	statusChange.inverterStatus = append(statusChange.inverterStatus, status)
	c[id] = statusChange

	for k, v := range c {
		statuses := strings.Join(v.inverterStatus, ",")
		fmt.Printf("applianceID: %s, inverterStatus: %s, counter: %d", k, statuses, v.counter)
		fmt.Println()
	}
	fmt.Println()
}

type CountStatusChange map[string]StatusChange

type StatusChange struct {
	inverterStatus []string
	counter        int
}

func main() {
	log.Printf("Server started")

	var counter CountStatusChange
	counter = make(map[string]StatusChange)
	WebhookReceiverAPIService := openapi.NewWebhookReceiverAPIService(counter)
	WebhookReceiverAPIController := openapi.NewWebhookReceiverAPIController(WebhookReceiverAPIService)

	router := openapi.NewRouter(WebhookReceiverAPIController)

	log.Fatal(http.ListenAndServe(":8080", router))
}
