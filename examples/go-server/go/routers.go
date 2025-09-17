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
	"net/http"

	"github.com/gorilla/mux"

	"github.com/grid-x/example-webhook-receiver/pkg/hmac"
)

// A Route defines the parameters for an api endpoint
type Route struct {
	Name        string
	Method      string
	Pattern     string
	HandlerFunc http.HandlerFunc
}

// Routes is a map of defined api endpoints
type Routes map[string]Route

// Router defines the required methods for retrieving api routes
type Router interface {
	Routes() Routes
	OrderedRoutes() []Route
}

// NewRouter creates a new router for any number of api routers
func NewRouter(routers []Router, verifier *hmac.RequestVerifier) *mux.Router {
	router := mux.NewRouter().StrictSlash(true)
	for _, api := range routers {
		for _, route := range api.OrderedRoutes() {
			var handler http.Handler = route.HandlerFunc
			handler = Logger(handler, route.Name)
			handler = verifier.Middleware(handler)
			router.
				Methods(route.Method).
				Path(route.Pattern).
				Name(route.Name).
				Handler(handler)
		}
	}

	return router
}
