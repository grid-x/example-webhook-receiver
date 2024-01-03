# Event

Event which follows the [CloudEvents v1.0.1 specification](https://github.com/cloudevents/spec/blob/v1.0.1/spec.md).  An event consists of metadata (such as occurrence time and ID) and the actual `data` payload that depends on the event's `type`. The extension attribute `notification` can be used by consumers to produce a notification. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time** | **datetime** | Time when the event has occurred in RFC3339 format. | 
**type** | **str** | Type of the event, can be used to determine how the &#x60;data&#x60; payload is deserialized. | 
**data_content_type** | **str** | Content-Type indicating how to parse the &#x60;data&#x60; attribute. Only &#39;application/json&#39; is supported for now. If ommitted, it is guaranteed to be &#x60;application/json&#x60;. | [optional] [default to 'application/json']
**spec_version** | **str** | The CloudEvents specification that is followed, currently \&quot;1.0\&quot;. Only consists of major and minor version parts, to allow patching in a backward-compatible fashion. | 
**data** | [**EventData**](EventData.md) |  | [optional] 
**source** | **str** | Source of the event, which is usually a resource identifier path that can be used to identify the object which triggered the event. | 
**correlation_id** | **str** | ID to identify the request triggering the event. | [optional] 
**notification** | [**Notification**](Notification.md) |  | [optional] 

## Example

```python
from openapi_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print Event.to_json()

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_form_dict = event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


