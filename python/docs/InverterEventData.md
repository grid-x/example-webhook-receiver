# InverterEventData

Payload for `inverter/*` events. The event describes the change of an inverter from one status to a new one. The old status is referred to as the lastStatus. 

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
**status** | **str** | Current (new) status of the inverter. | 
**last_status** | **str** | Last status of the inverter. | 
**err_code** | **str** | Current (new) error code as returned by the appliance. The value depends on the appliance manufacturer, model and firmware. Please refer to the manufacturers specification.  | [optional] 
**last_err_code** | **str** | Last error code as returned by the appliance. The value depends on the appliance manufacturer, model and firmware. Please refer to the manufacturers specification.  | [optional] 

## Example

```python
from openapi_client.models.inverter_event_data import InverterEventData

# TODO update the JSON string below
json = "{}"
# create an instance of InverterEventData from a JSON string
inverter_event_data_instance = InverterEventData.from_json(json)
# print the JSON string representation of the object
print InverterEventData.to_json()

# convert the object into a dict
inverter_event_data_dict = inverter_event_data_instance.to_dict()
# create an instance of InverterEventData from a dict
inverter_event_data_form_dict = inverter_event_data.from_dict(inverter_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


