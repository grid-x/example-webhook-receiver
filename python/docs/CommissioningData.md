# CommissioningData

Payload for `commissioning/done` events.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | The ID of the newly created customer after the commissioning process. | [optional] 
**customer_email** | **str** | The email of the newly created customer after the commissioning process. | [optional] 
**customer_address** | **str** | The address of the newly created customer after the commissioning process. | [optional] 
**system_name** | **str** | The name of the commissioned system. | [optional] 
**gateway_serialnumber** | **str** | The serialnumber of the gateway corresponding to the commissioned system. | [optional] 

## Example

```python
from openapi_client.models.commissioning_data import CommissioningData

# TODO update the JSON string below
json = "{}"
# create an instance of CommissioningData from a JSON string
commissioning_data_instance = CommissioningData.from_json(json)
# print the JSON string representation of the object
print CommissioningData.to_json()

# convert the object into a dict
commissioning_data_dict = commissioning_data_instance.to_dict()
# create an instance of CommissioningData from a dict
commissioning_data_form_dict = commissioning_data.from_dict(commissioning_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


