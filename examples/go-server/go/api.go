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
	"context"
	"net/http"
)

// DefaultAPIRouter defines the required methods for binding the api requests to a responses for the DefaultAPI
// The DefaultAPIRouter implementation should parse necessary information from the http request,
// pass the data to a DefaultAPIServicer to perform the required actions, then write the service results to the http response.
type DefaultAPIRouter interface {
	ProcessXenonWebhookEvent(http.ResponseWriter, *http.Request)
}

// DefaultAPIServicer defines the api actions for the DefaultAPI service
// This interface intended to stay up to date with the openapi yaml used to generate it,
// while the service implementation can be ignored with the .openapi-generator-ignore file
// and updated with the logic required for the API.
type DefaultAPIServicer interface {
	ProcessXenonWebhookEvent(context.Context, WebhookEventRequest) (ImplResponse, error)
}
