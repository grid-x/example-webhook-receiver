# coding: utf-8

"""
    Webhook Event Receiver API

    This API describes the event webhook calling convention. In order to receive webhook events from the gridX API, third parties must implement endpoints according to this specification. In the following, the external partner API is referred to as  \"external API\", while the gridX API is called \"gridX\". 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from openapi_client.models.appliance_event_data import ApplianceEventData
from openapi_client.models.commissioning_data import CommissioningData
from openapi_client.models.ev_event_data import EVEventData
from openapi_client.models.gateway_event_data import GatewayEventData
from openapi_client.models.inverter_event_data import InverterEventData
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

EVENTDATA_ONE_OF_SCHEMAS = ["ApplianceEventData", "CommissioningData", "EVEventData", "GatewayEventData", "InverterEventData"]

class EventData(BaseModel):
    """
    Domain-specific data depending on the `type` of the event.
    """
    # data type: ApplianceEventData
    oneof_schema_1_validator: Optional[ApplianceEventData] = None
    # data type: InverterEventData
    oneof_schema_2_validator: Optional[InverterEventData] = None
    # data type: GatewayEventData
    oneof_schema_3_validator: Optional[GatewayEventData] = None
    # data type: EVEventData
    oneof_schema_4_validator: Optional[EVEventData] = None
    # data type: CommissioningData
    oneof_schema_5_validator: Optional[CommissioningData] = None
    if TYPE_CHECKING:
        actual_instance: Union[ApplianceEventData, CommissioningData, EVEventData, GatewayEventData, InverterEventData]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(EVENTDATA_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = EventData.construct()
        error_messages = []
        match = 0
        # validate data type: ApplianceEventData
        if not isinstance(v, ApplianceEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApplianceEventData`")
        else:
            match += 1
        # validate data type: InverterEventData
        if not isinstance(v, InverterEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InverterEventData`")
        else:
            match += 1
        # validate data type: GatewayEventData
        if not isinstance(v, GatewayEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GatewayEventData`")
        else:
            match += 1
        # validate data type: EVEventData
        if not isinstance(v, EVEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EVEventData`")
        else:
            match += 1
        # validate data type: CommissioningData
        if not isinstance(v, CommissioningData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CommissioningData`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in EventData with oneOf schemas: ApplianceEventData, CommissioningData, EVEventData, GatewayEventData, InverterEventData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in EventData with oneOf schemas: ApplianceEventData, CommissioningData, EVEventData, GatewayEventData, InverterEventData. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> EventData:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> EventData:
        """Returns the object represented by the json string"""
        instance = EventData.construct()
        error_messages = []
        match = 0

        # deserialize data into ApplianceEventData
        try:
            instance.actual_instance = ApplianceEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InverterEventData
        try:
            instance.actual_instance = InverterEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GatewayEventData
        try:
            instance.actual_instance = GatewayEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EVEventData
        try:
            instance.actual_instance = EVEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CommissioningData
        try:
            instance.actual_instance = CommissioningData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into EventData with oneOf schemas: ApplianceEventData, CommissioningData, EVEventData, GatewayEventData, InverterEventData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into EventData with oneOf schemas: ApplianceEventData, CommissioningData, EVEventData, GatewayEventData, InverterEventData. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


