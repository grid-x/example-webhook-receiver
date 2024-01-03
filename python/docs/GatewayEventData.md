# GatewayEventData

Payload for `gateway/*` events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_id** | **str** | The ID of the gateway this event is triggered for. | 
**gateway_name** | **str** | The name of the gateway corresponding to the gatewayID. | [optional] 
**gateway_serialnumber** | **str** | The serialnumber of the gateway corresponding to the gatewayID. | [optional] 
**system_id** | **str** | The ID of the system this event is triggered for. | 
**system_name** | **str** | The name of the system corresponding to the systemID. | [optional] 
**user_id** | **str** | The ID of the user that owns the system. | [optional] 
**user_name** | **str** | Name of the user belonging to the userID. | [optional] 
**user_mail** | **str** | E-Mail address of the user belonging to the userID. | [optional] 

## Example

```python
from openapi_client.models.gateway_event_data import GatewayEventData

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayEventData from a JSON string
gateway_event_data_instance = GatewayEventData.from_json(json)
# print the JSON string representation of the object
print GatewayEventData.to_json()

# convert the object into a dict
gateway_event_data_dict = gateway_event_data_instance.to_dict()
# create an instance of GatewayEventData from a dict
gateway_event_data_form_dict = gateway_event_data.from_dict(gateway_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


