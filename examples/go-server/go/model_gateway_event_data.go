// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

/*
 * gridX Webhook Event Receiver API
 *
 * This API describes the event webhook calling convention. In order to receive webhook events from the gridX API, third parties must implement endpoints according to this specification. In the following, the external partner API is referred to as  \"external API\", while the gridX API is called \"gridX\". 
 *
 * API version: 1.0.0
 */

package openapi




// GatewayEventData - Payload for `gateway/_*` events.
type GatewayEventData struct {

	// The ID of the gateway this event is triggered for.
	GatewayID string `json:"gatewayID"`

	// The name of the gateway corresponding to the gatewayID.
	GatewayName string `json:"gatewayName,omitempty"`

	// The serialnumber of the gateway corresponding to the gatewayID.
	GatewaySerialnumber string `json:"gatewaySerialnumber,omitempty"`

	// The ID of the system this event is triggered for.
	SystemID string `json:"systemID"`

	// The name of the system corresponding to the systemID.
	SystemName string `json:"systemName,omitempty"`

	// The ID of the user that owns the system.
	UserID string `json:"userID,omitempty"`

	// Name of the user belonging to the userID.
	UserName string `json:"userName,omitempty"`

	// E-Mail address of the user belonging to the userID.
	UserMail string `json:"userMail,omitempty"`
}

// AssertGatewayEventDataRequired checks if the required fields are not zero-ed
func AssertGatewayEventDataRequired(obj GatewayEventData) error {
	elements := map[string]interface{}{
		"gatewayID": obj.GatewayID,
		"systemID": obj.SystemID,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	return nil
}

// AssertGatewayEventDataConstraints checks if the values respects the defined constraints
func AssertGatewayEventDataConstraints(obj GatewayEventData) error {
	return nil
}
