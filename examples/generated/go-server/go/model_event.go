/*
 * Webhook Event Receiver API
 *
 * This API describes the event webhook calling convention. In order to receive webhook events from the gridX API, third parties must implement endpoints according to this specification. In the following, the external partner API is referred to as  \"external API\", while the gridX API is called \"gridX\". 
 *
 * API version: 1.0.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi


import (
	"time"
)



// Event - Event which follows the [CloudEvents v1.0.1 specification](https://github.com/cloudevents/spec/blob/v1.0.1/spec.md).  An event consists of metadata (such as occurrence time and ID) and the actual `data` payload that depends on the event's `type`. The extension attribute `notification` can be used by consumers to produce a notification. 
type Event struct {

	Id string `json:"id"`

	// Time when the event has occurred in RFC3339 format.
	Time time.Time `json:"time"`

	// Type of the event, can be used to determine how the `data` payload is deserialized.
	Type string `json:"type"`

	// Content-Type indicating how to parse the `data` attribute. Only 'application/json' is supported for now. If ommitted, it is guaranteed to be `application/json`.
	DataContentType string `json:"dataContentType,omitempty"`

	// The CloudEvents specification that is followed, currently \"1.0\". Only consists of major and minor version parts, to allow patching in a backward-compatible fashion.
	SpecVersion string `json:"specVersion"`

	Data ApplianceEventData `json:"data,omitempty"`

	// Source of the event, which is usually a resource identifier path that can be used to identify the object which triggered the event.
	Source string `json:"source"`

	// ID to identify the request triggering the event.
	CorrelationID string `json:"correlationID,omitempty"`

	Notification Notification `json:"notification,omitempty"`
}

// AssertEventRequired checks if the required fields are not zero-ed
func AssertEventRequired(obj Event) error {
	elements := map[string]interface{}{
		"id": obj.Id,
		"time": obj.Time,
		"type": obj.Type,
		"specVersion": obj.SpecVersion,
		"source": obj.Source,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	if err := AssertApplianceEventDataRequired(obj.Data); err != nil {
		return err
	}
	if err := AssertNotificationRequired(obj.Notification); err != nil {
		return err
	}
	return nil
}

// AssertEventConstraints checks if the values respects the defined constraints
func AssertEventConstraints(obj Event) error {
	return nil
}
