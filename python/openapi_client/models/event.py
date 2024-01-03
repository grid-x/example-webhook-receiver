# coding: utf-8

"""
    Webhook Event Receiver API

    This API describes the event webhook calling convention. In order to receive webhook events from the gridX API, third parties must implement endpoints according to this specification. In the following, the external partner API is referred to as  \"external API\", while the gridX API is called \"gridX\". 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.event_data import EventData
from openapi_client.models.notification import Notification

class Event(BaseModel):
    """
    Event which follows the [CloudEvents v1.0.1 specification](https://github.com/cloudevents/spec/blob/v1.0.1/spec.md).  An event consists of metadata (such as occurrence time and ID) and the actual `data` payload that depends on the event's `type`. The extension attribute `notification` can be used by consumers to produce a notification.   # noqa: E501
    """
    id: StrictStr = Field(...)
    time: datetime = Field(..., description="Time when the event has occurred in RFC3339 format.")
    type: StrictStr = Field(..., description="Type of the event, can be used to determine how the `data` payload is deserialized.")
    data_content_type: Optional[StrictStr] = Field('application/json', alias="dataContentType", description="Content-Type indicating how to parse the `data` attribute. Only 'application/json' is supported for now. If ommitted, it is guaranteed to be `application/json`.")
    spec_version: StrictStr = Field(..., alias="specVersion", description="The CloudEvents specification that is followed, currently \"1.0\". Only consists of major and minor version parts, to allow patching in a backward-compatible fashion.")
    data: Optional[EventData] = None
    source: StrictStr = Field(..., description="Source of the event, which is usually a resource identifier path that can be used to identify the object which triggered the event.")
    correlation_id: Optional[StrictStr] = Field(None, alias="correlationID", description="ID to identify the request triggering the event.")
    notification: Optional[Notification] = None
    __properties = ["id", "time", "type", "dataContentType", "specVersion", "data", "source", "correlationID", "notification"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('appliance/create', 'appliance/offline', 'appliance/online', 'inverter/status', 'gateway/create', 'gateway/offline', 'gateway/online', 'ev/plugged', 'commissioning/done'):
            raise ValueError("must be one of enum values ('appliance/create', 'appliance/offline', 'appliance/online', 'inverter/status', 'gateway/create', 'gateway/offline', 'gateway/online', 'ev/plugged', 'commissioning/done')")
        return value

    @validator('data_content_type')
    def data_content_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('application/json'):
            raise ValueError("must be one of enum values ('application/json')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Event:
        """Create an instance of Event from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notification
        if self.notification:
            _dict['notification'] = self.notification.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Event:
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Event.parse_obj(obj)

        _obj = Event.parse_obj({
            "id": obj.get("id"),
            "time": obj.get("time"),
            "type": obj.get("type"),
            "data_content_type": obj.get("dataContentType") if obj.get("dataContentType") is not None else 'application/json',
            "spec_version": obj.get("specVersion"),
            "data": EventData.from_dict(obj.get("data")) if obj.get("data") is not None else None,
            "source": obj.get("source"),
            "correlation_id": obj.get("correlationID"),
            "notification": Notification.from_dict(obj.get("notification")) if obj.get("notification") is not None else None
        })
        return _obj


