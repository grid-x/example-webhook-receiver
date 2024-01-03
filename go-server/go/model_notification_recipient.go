/*
 * Webhook Event Receiver API
 *
 * This API describes the event webhook calling convention. In order to receive webhook events from the gridX API, third parties must implement endpoints according to this specification. In the following, the external partner API is referred to as  \"external API\", while the gridX API is called \"gridX\". 
 *
 * API version: 1.0.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi




type NotificationRecipient struct {

	// User ID for identifying the user via gridX API.
	UserID string `json:"userID,omitempty"`

	// Account ID for identifying the user via gridX API.
	AccountID string `json:"accountID,omitempty"`

	// Email address of the recipient.
	Email string `json:"email,omitempty"`

	// Full name of the recipient if available.
	FullName string `json:"fullName,omitempty"`

	// Determined locale of the user in format of a language tag, `<language>_<COUNTRY>`, e.g. `en_GB`.
	Locale string `json:"locale,omitempty"`
}

// AssertNotificationRecipientRequired checks if the required fields are not zero-ed
func AssertNotificationRecipientRequired(obj NotificationRecipient) error {
	return nil
}

// AssertNotificationRecipientConstraints checks if the values respects the defined constraints
func AssertNotificationRecipientConstraints(obj NotificationRecipient) error {
	return nil
}
