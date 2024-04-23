// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

/*
 * gridX Webhook Event Receiver API
 *
 * This API describes the event webhook calling convention. In order to receive webhook events from the gridX API, third parties must implement endpoints according to this specification. In the following, the external partner API is referred to as  \"external API\", while the gridX API is called \"gridX\". 
 *
 * API version: 1.0.0
 */

package openapi




// InverterEventData - Payload for `inverter/_*` events. The event describes the change of an inverter from one status to a new one. The old status is referred to as the lastStatus. 
type InverterEventData struct {

	// ID of the appliance that caused this event.
	ApplianceID string `json:"applianceID"`

	// The ID of the gateway that connects to the appliance.
	GatewayID string `json:"gatewayID"`

	// Model description of the appliance.
	Model string `json:"model,omitempty"`

	// Manufacturer of the appliance.
	Manufacturer string `json:"manufacturer,omitempty"`

	// General type of the appliance.
	Type string `json:"type,omitempty"`

	// Kind of the appliance is used to provide further details on the appliance configuration and mode of operation. The kind property is only available for appliances with type INVERTER or METER. For inverters, only UNKNOWN, PV, BATTERY, HYBRID and PV_EXTERNAL are valid values. They describe the  kind of connected appliance(s) and define the role of the inverter in the system. For meters, kind specifies the appliance the meter is attached to. It resembles the location the meter is installed in. 
	Kind string `json:"kind,omitempty"`

	// The name of the appliance as defined by the customer.
	Name string `json:"name,omitempty"`

	// Serial number of the appliance as returned by the appliance.
	SerialNumber string `json:"serialNumber,omitempty"`

	// The ID of the system that the gateway and appliance run in.
	SystemID string `json:"systemID"`

	// Name of the system as defined by the customer.
	SystemName string `json:"systemName,omitempty"`

	// Current (new) status of the inverter.
	Status string `json:"status"`

	// Last status of the inverter.
	LastStatus string `json:"lastStatus"`

	// Current (new) error code as returned by the appliance. The value depends on the appliance manufacturer, model and firmware. Please refer to the manufacturers specification. 
	ErrCode string `json:"errCode,omitempty"`

	// Last error code as returned by the appliance. The value depends on the appliance manufacturer, model and firmware. Please refer to the manufacturers specification. 
	LastErrCode string `json:"lastErrCode,omitempty"`
}

// AssertInverterEventDataRequired checks if the required fields are not zero-ed
func AssertInverterEventDataRequired(obj InverterEventData) error {
	elements := map[string]interface{}{
		"applianceID": obj.ApplianceID,
		"gatewayID": obj.GatewayID,
		"systemID": obj.SystemID,
		"status": obj.Status,
		"lastStatus": obj.LastStatus,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	return nil
}

// AssertInverterEventDataConstraints checks if the values respects the defined constraints
func AssertInverterEventDataConstraints(obj InverterEventData) error {
	return nil
}
