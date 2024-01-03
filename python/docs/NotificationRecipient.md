# NotificationRecipient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID for identifying the user via gridX API. | [optional] 
**account_id** | **str** | Account ID for identifying the user via gridX API. | [optional] 
**email** | **str** | Email address of the recipient. | [optional] 
**full_name** | **str** | Full name of the recipient if available. | [optional] 
**locale** | **str** | Determined locale of the user in format of a language tag, &#x60;&lt;language&gt;_&lt;COUNTRY&gt;&#x60;, e.g. &#x60;en_GB&#x60;. | [optional] 

## Example

```python
from openapi_client.models.notification_recipient import NotificationRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRecipient from a JSON string
notification_recipient_instance = NotificationRecipient.from_json(json)
# print the JSON string representation of the object
print NotificationRecipient.to_json()

# convert the object into a dict
notification_recipient_dict = notification_recipient_instance.to_dict()
# create an instance of NotificationRecipient from a dict
notification_recipient_form_dict = notification_recipient.from_dict(notification_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


