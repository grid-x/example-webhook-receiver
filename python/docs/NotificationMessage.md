# NotificationMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** | Title of the message, in the &#x60;locale&#x60; of the &#x60;recipient&#x60;. Subject to changes at any time. | [optional] 
**text_content_type** | **str** | Content-Type of the &#x60;text&#x60; attribute. | [optional] 
**text** | **str** | Exemplary text message in the &#x60;locale&#x60; of the &#x60;recipient&#x60;. Subject to changes at any time. | [optional] 
**action_url** | **str** | URL that links to further information about the event&#39;s origin, usable for call-to-action buttons. | [optional] 

## Example

```python
from openapi_client.models.notification_message import NotificationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationMessage from a JSON string
notification_message_instance = NotificationMessage.from_json(json)
# print the JSON string representation of the object
print NotificationMessage.to_json()

# convert the object into a dict
notification_message_dict = notification_message_instance.to_dict()
# create an instance of NotificationMessage from a dict
notification_message_form_dict = notification_message.from_dict(notification_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


