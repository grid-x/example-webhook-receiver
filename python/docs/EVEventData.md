# EVEventData

Payload for `ev/*` events. The event describes the change of an EV's state at a charging station. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliance_id** | **str** | ID of the appliance that caused this event. | 
**gateway_id** | **str** | The ID of the gateway that connects to the appliance. | 
**model** | **str** | Model description of the appliance. | [optional] 
**manufacturer** | **str** | Manufacturer of the appliance. | [optional] 
**type** | **str** | General type of the appliance. | [optional] 
**kind** | **str** | Kind of the appliance is used to provide further details on the appliance configuration and mode of operation. The kind property is only available for appliances with type INVERTER or METER. For inverters, only UNKNOWN, PV, BATTERY, HYBRID and PV_EXTERNAL are valid values. They describe the  kind of connected appliance(s) and define the role of the inverter in the system. For meters, kind specifies the appliance the meter is attached to. It resembles the location the meter is installed in.  | [optional] 
**name** | **str** | The name of the appliance as defined by the customer. | [optional] 
**serial_number** | **str** | Serial number of the appliance as returned by the appliance. | [optional] 
**system_id** | **str** | The ID of the system that the gateway and appliance run in. | 
**system_name** | **str** | Name of the system as defined by the customer. | [optional] 
**evse_id** | **str** | Electirc Vehicle Supply Equipment ID | [optional] 
**state** | **str** | State of the EV charging station. | 

## Example

```python
from openapi_client.models.ev_event_data import EVEventData

# TODO update the JSON string below
json = "{}"
# create an instance of EVEventData from a JSON string
ev_event_data_instance = EVEventData.from_json(json)
# print the JSON string representation of the object
print EVEventData.to_json()

# convert the object into a dict
ev_event_data_dict = ev_event_data_instance.to_dict()
# create an instance of EVEventData from a dict
ev_event_data_form_dict = ev_event_data.from_dict(ev_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


