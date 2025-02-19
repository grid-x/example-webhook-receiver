/*
 * gridX Webhook Event Receiver API
 *
 * This API describes the event webhook calling convention. In order to receive webhook events from the gridX API, third parties must implement endpoints according to this specification. In the following, the external partner API is referred to as  \"external API\", while the gridX API is called \"gridX\".
 *
 * API version: 1.0.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi

import (
	"context"
	"errors"
	"net/http"
)

// WebhookReceiverAPIService is a service that implements the logic for the WebhookReceiverAPIServicer
// This service should implement the business logic for every endpoint for the WebhookReceiverAPI API.
// Include any external packages or services that will be required by this service.
type WebhookReceiverAPIService struct {
	statusChangeCounter CountStatusChange
}

type CountStatusChange interface {
	Increment(id string, status string)
}

// NewWebhookReceiverAPIService creates a default api service
func NewWebhookReceiverAPIService(counter CountStatusChange) WebhookReceiverAPIServicer {
	return &WebhookReceiverAPIService{statusChangeCounter: counter}
}

// EventsApplianceCreatePost - Webhook Receiver
func (s *WebhookReceiverAPIService) EventsApplianceCreatePost(ctx context.Context, xSignature string, applianceCreateEvent ApplianceCreateEvent) (ImplResponse, error) {
	// TODO - update EventsApplianceCreatePost with the required logic for this service method.
	// Add api_webhook_receiver_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, {}) or use other options such as http.Ok ...
	// return Response(200, nil),nil

	// TODO: Uncomment the next line to return response Response(403, {}) or use other options such as http.Ok ...
	// return Response(403, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	// TODO: Uncomment the next line to return response Response(500, {}) or use other options such as http.Ok ...
	// return Response(500, nil),nil

	// TODO: Uncomment the next line to return response Response(503, {}) or use other options such as http.Ok ...
	// return Response(503, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("EventsApplianceCreatePost method not implemented")
}

// EventsApplianceOfflinePost - Webhook Receiver
func (s *WebhookReceiverAPIService) EventsApplianceOfflinePost(ctx context.Context, xSignature string, applianceOfflineEvent ApplianceOfflineEvent) (ImplResponse, error) {
	// TODO - update EventsApplianceOfflinePost with the required logic for this service method.
	// Add api_webhook_receiver_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, {}) or use other options such as http.Ok ...
	// return Response(200, nil),nil

	// TODO: Uncomment the next line to return response Response(403, {}) or use other options such as http.Ok ...
	// return Response(403, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	// TODO: Uncomment the next line to return response Response(500, {}) or use other options such as http.Ok ...
	// return Response(500, nil),nil

	// TODO: Uncomment the next line to return response Response(503, {}) or use other options such as http.Ok ...
	// return Response(503, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("EventsApplianceOfflinePost method not implemented")
}

// EventsApplianceOnlinePost - Webhook Receiver
func (s *WebhookReceiverAPIService) EventsApplianceOnlinePost(ctx context.Context, xSignature string, applianceOnlineEvent ApplianceOnlineEvent) (ImplResponse, error) {
	// TODO - update EventsApplianceOnlinePost with the required logic for this service method.
	// Add api_webhook_receiver_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, {}) or use other options such as http.Ok ...
	// return Response(200, nil),nil

	// TODO: Uncomment the next line to return response Response(403, {}) or use other options such as http.Ok ...
	// return Response(403, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	// TODO: Uncomment the next line to return response Response(500, {}) or use other options such as http.Ok ...
	// return Response(500, nil),nil

	// TODO: Uncomment the next line to return response Response(503, {}) or use other options such as http.Ok ...
	// return Response(503, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("EventsApplianceOnlinePost method not implemented")
}

// EventsComissioningDonePost - Webhook Receiver
func (s *WebhookReceiverAPIService) EventsComissioningDonePost(ctx context.Context, xSignature string, comissioningDoneEvent ComissioningDoneEvent) (ImplResponse, error) {
	// TODO - update EventsComissioningDonePost with the required logic for this service method.
	// Add api_webhook_receiver_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, {}) or use other options such as http.Ok ...
	// return Response(200, nil),nil

	// TODO: Uncomment the next line to return response Response(403, {}) or use other options such as http.Ok ...
	// return Response(403, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	// TODO: Uncomment the next line to return response Response(500, {}) or use other options such as http.Ok ...
	// return Response(500, nil),nil

	// TODO: Uncomment the next line to return response Response(503, {}) or use other options such as http.Ok ...
	// return Response(503, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("EventsComissioningDonePost method not implemented")
}

// EventsEvPluggedPost - Webhook Receiver
func (s *WebhookReceiverAPIService) EventsEvPluggedPost(ctx context.Context, xSignature string, evPluggedEvent EvPluggedEvent) (ImplResponse, error) {
	// TODO - update EventsEvPluggedPost with the required logic for this service method.
	// Add api_webhook_receiver_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, {}) or use other options such as http.Ok ...
	// return Response(200, nil),nil

	// TODO: Uncomment the next line to return response Response(403, {}) or use other options such as http.Ok ...
	// return Response(403, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	// TODO: Uncomment the next line to return response Response(500, {}) or use other options such as http.Ok ...
	// return Response(500, nil),nil

	// TODO: Uncomment the next line to return response Response(503, {}) or use other options such as http.Ok ...
	// return Response(503, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("EventsEvPluggedPost method not implemented")
}

// EventsGatewayCreatePost - Webhook Receiver
func (s *WebhookReceiverAPIService) EventsGatewayCreatePost(ctx context.Context, xSignature string, gatewayCreateEvent GatewayCreateEvent) (ImplResponse, error) {
	// TODO - update EventsGatewayCreatePost with the required logic for this service method.
	// Add api_webhook_receiver_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, {}) or use other options such as http.Ok ...
	// return Response(200, nil),nil

	// TODO: Uncomment the next line to return response Response(403, {}) or use other options such as http.Ok ...
	// return Response(403, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	// TODO: Uncomment the next line to return response Response(500, {}) or use other options such as http.Ok ...
	// return Response(500, nil),nil

	// TODO: Uncomment the next line to return response Response(503, {}) or use other options such as http.Ok ...
	// return Response(503, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("EventsGatewayCreatePost method not implemented")
}

// EventsGatewayOfflinePost - Webhook Receiver
func (s *WebhookReceiverAPIService) EventsGatewayOfflinePost(ctx context.Context, xSignature string, gatewayOfflineEvent GatewayOfflineEvent) (ImplResponse, error) {
	// TODO - update EventsGatewayOfflinePost with the required logic for this service method.
	// Add api_webhook_receiver_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, {}) or use other options such as http.Ok ...
	// return Response(200, nil),nil

	// TODO: Uncomment the next line to return response Response(403, {}) or use other options such as http.Ok ...
	// return Response(403, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	// TODO: Uncomment the next line to return response Response(500, {}) or use other options such as http.Ok ...
	// return Response(500, nil),nil

	// TODO: Uncomment the next line to return response Response(503, {}) or use other options such as http.Ok ...
	// return Response(503, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("EventsGatewayOfflinePost method not implemented")
}

// EventsGatewayOnlinePost - Webhook Receiver
func (s *WebhookReceiverAPIService) EventsGatewayOnlinePost(ctx context.Context, xSignature string, gatewayOnlineEvent GatewayOnlineEvent) (ImplResponse, error) {
	// TODO - update EventsGatewayOnlinePost with the required logic for this service method.
	// Add api_webhook_receiver_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, {}) or use other options such as http.Ok ...
	// return Response(200, nil),nil

	// TODO: Uncomment the next line to return response Response(403, {}) or use other options such as http.Ok ...
	// return Response(403, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	// TODO: Uncomment the next line to return response Response(500, {}) or use other options such as http.Ok ...
	// return Response(500, nil),nil

	// TODO: Uncomment the next line to return response Response(503, {}) or use other options such as http.Ok ...
	// return Response(503, nil),nil

	return Response(http.StatusNotImplemented, nil), errors.New("EventsGatewayOnlinePost method not implemented")
}

// EventsInverterStatusPost - Webhook Receiver
func (s *WebhookReceiverAPIService) EventsInverterStatusPost(ctx context.Context, xSignature string, inverterStatusEvent InverterStatusEvent) (ImplResponse, error) {
	// TODO - update EventsInverterStatusPost with the required logic for this service method.
	// Add api_webhook_receiver_service.go to the .openapi-generator-ignore to avoid overwriting this service implementation when updating open api generation.

	// TODO: Uncomment the next line to return response Response(200, {}) or use other options such as http.Ok ...
	// return Response(200, nil),nil

	// TODO: Uncomment the next line to return response Response(403, {}) or use other options such as http.Ok ...
	// return Response(403, nil),nil

	// TODO: Uncomment the next line to return response Response(404, {}) or use other options such as http.Ok ...
	// return Response(404, nil),nil

	// TODO: Uncomment the next line to return response Response(500, {}) or use other options such as http.Ok ...
	// return Response(500, nil),nil

	// TODO: Uncomment the next line to return response Response(503, {}) or use other options such as http.Ok ...
	// return Response(503, nil),nil
	s.statusChangeCounter.Increment(inverterStatusEvent.Data.ApplianceID, inverterStatusEvent.Data.Status)
	return Response(http.StatusAccepted, inverterStatusEvent), errors.New("EventsInverterStatusPost method not implemented")
}
