# EventData

Domain-specific data depending on the `type` of the event.

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
**system_name** | **str** | The name of the commissioned system. | [optional] 
**status** | **str** | Current (new) status of the inverter. | 
**last_status** | **str** | Last status of the inverter. | 
**err_code** | **str** | Current (new) error code as returned by the appliance. The value depends on the appliance manufacturer, model and firmware. Please refer to the manufacturers specification.  | [optional] 
**last_err_code** | **str** | Last error code as returned by the appliance. The value depends on the appliance manufacturer, model and firmware. Please refer to the manufacturers specification.  | [optional] 
**gateway_name** | **str** | The name of the gateway corresponding to the gatewayID. | [optional] 
**gateway_serialnumber** | **str** | The serialnumber of the gateway corresponding to the commissioned system. | [optional] 
**user_id** | **str** | The ID of the user that owns the system. | [optional] 
**user_name** | **str** | Name of the user belonging to the userID. | [optional] 
**user_mail** | **str** | E-Mail address of the user belonging to the userID. | [optional] 
**evse_id** | **str** | Electirc Vehicle Supply Equipment ID | [optional] 
**state** | **str** | State of the EV charging station. | 
**customer_id** | **str** | The ID of the newly created customer after the commissioning process. | [optional] 
**customer_email** | **str** | The email of the newly created customer after the commissioning process. | [optional] 
**customer_address** | **str** | The address of the newly created customer after the commissioning process. | [optional] 

## Example

```python
from openapi_client.models.event_data import EventData

# TODO update the JSON string below
json = "{}"
# create an instance of EventData from a JSON string
event_data_instance = EventData.from_json(json)
# print the JSON string representation of the object
print EventData.to_json()

# convert the object into a dict
event_data_dict = event_data_instance.to_dict()
# create an instance of EventData from a dict
event_data_form_dict = event_data.from_dict(event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


