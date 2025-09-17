/*
 * Example XENON webhook receiver
 *
 * This is an example webhook receiver for XENON.
 *
 * API version: v1.0.0
 * Contact: developer-community@gridx.de
 */

package openapi

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
)

// DefaultAPIService is a service that implements the logic for the DefaultAPIServicer
// This service should implement the business logic for every endpoint for the DefaultAPI API.
// Include any external packages or services that will be required by this service.
type DefaultAPIService struct {
}

// NewDefaultAPIService creates a default api service
func NewDefaultAPIService() *DefaultAPIService {
	return &DefaultAPIService{}
}

// ProcessXenonWebhookEvent -
func (s *DefaultAPIService) ProcessXenonWebhookEvent(ctx context.Context, webhookEventRequest WebhookEventRequest) (ImplResponse, error) {
	// TODO - update ProcessXenonWebhookEvent with the required logic for this service method.
	if webhookEventRequest.Type == "appliance/create" ||
		webhookEventRequest.Type == "appliance/update" ||
		webhookEventRequest.Type == "appliance/delete" ||
		webhookEventRequest.Type == "appliance/online" ||
		webhookEventRequest.Type == "appliance/offline" {
		var data ApplianceEvent
		if err := json.Unmarshal(webhookEventRequest.Data, &data); err != nil {
			return Response(http.StatusUnprocessableEntity, map[string]interface{}{}), nil
		}

		var pretty bytes.Buffer
		err := json.Indent(&pretty, webhookEventRequest.Data, "", "  ")
		if err != nil {
			return Response(http.StatusUnprocessableEntity, map[string]interface{}{}), nil
		}

		fmt.Printf("event %s with %s", webhookEventRequest.Type, pretty.String())
		return Response(http.StatusAccepted, map[string]interface{}{}), nil
	}

	if webhookEventRequest.Type == "ev/plugged" ||
		webhookEventRequest.Type == "ev/unplugged" {
		var data EvPluggedEvent
		if err := json.Unmarshal(webhookEventRequest.Data, &data); err != nil {
			fmt.Printf("failed to unmarshal event %s: %s", string(webhookEventRequest.Data), err)
			return Response(http.StatusUnprocessableEntity, map[string]interface{}{}), nil
		}

		var pretty bytes.Buffer
		err := json.Indent(&pretty, webhookEventRequest.Data, "", "  ")
		if err != nil {
			return Response(http.StatusUnprocessableEntity, map[string]interface{}{}), nil
		}

		fmt.Printf("event %s with %s", webhookEventRequest.Type, pretty.String())
		return Response(http.StatusAccepted, map[string]interface{}{}), nil
	}

	if webhookEventRequest.Type == "ping" {
		log.Print("ping")
		return Response(http.StatusAccepted, map[string]interface{}{}), nil
	}

	// TODO: Uncomment the next line to return response Response(200, {}) or use other options such as http.Ok ...
	// return Response(200, nil),nil

	// TODO: Uncomment the next line to return response Response(201, {}) or use other options such as http.Ok ...
	// return Response(201, nil),nil

	// TODO: Uncomment the next line to return response Response(202, {}) or use other options such as http.Ok ...
	// return Response(202, nil),nil

	// TODO: Uncomment the next line to return response Response(204, {}) or use other options such as http.Ok ...
	// return Response(204, nil),nil

	// TODO: Uncomment the next line to return response Response(401, {}) or use other options such as http.Ok ...
	// return Response(401, nil),nil

	// TODO: Uncomment the next line to return response Response(410, {}) or use other options such as http.Ok ...
	// return Response(410, nil),nil

	// TODO: Uncomment the next line to return response Response(408, map[string]interface{}{}) or use other options such as http.Ok ...
	// return Response(408, map[string]interface{}{}), nil

	// TODO: Uncomment the next line to return response Response(429, map[string]interface{}{}) or use other options such as http.Ok ...
	// return Response(429, map[string]interface{}{}), nil

	// TODO: Uncomment the next line to return response Response(500, map[string]interface{}{}) or use other options such as http.Ok ...
	// return Response(500, map[string]interface{}{}), nil

	// TODO: Uncomment the next line to return response Response(502, map[string]interface{}{}) or use other options such as http.Ok ...
	// return Response(502, map[string]interface{}{}), nil

	// TODO: Uncomment the next line to return response Response(503, map[string]interface{}{}) or use other options such as http.Ok ...
	// return Response(503, map[string]interface{}{}), nil

	// TODO: Uncomment the next line to return response Response(504, map[string]interface{}{}) or use other options such as http.Ok ...
	// return Response(504, map[string]interface{}{}), nil

	// TODO: Uncomment the next line to return response Response(0, map[string]interface{}{}) or use other options such as http.Ok ...
	// return Response(0, map[string]interface{}{}), nil

	return Response(http.StatusNotImplemented, nil), errors.New("ProcessXenonWebhookEvent method not implemented")
}
