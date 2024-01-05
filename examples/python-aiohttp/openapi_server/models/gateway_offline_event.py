# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.gateway_event_data import GatewayEventData
from openapi_server import util


class GatewayOfflineEvent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, time: datetime=None, data_content_type: str='application/json', spec_version: str=None, source: str=None, correlation_id: str=None, type: str=None, data: GatewayEventData=None):
        """GatewayOfflineEvent - a model defined in OpenAPI

        :param id: The id of this GatewayOfflineEvent.
        :param time: The time of this GatewayOfflineEvent.
        :param data_content_type: The data_content_type of this GatewayOfflineEvent.
        :param spec_version: The spec_version of this GatewayOfflineEvent.
        :param source: The source of this GatewayOfflineEvent.
        :param correlation_id: The correlation_id of this GatewayOfflineEvent.
        :param type: The type of this GatewayOfflineEvent.
        :param data: The data of this GatewayOfflineEvent.
        """
        self.openapi_types = {
            'id': str,
            'time': datetime,
            'data_content_type': str,
            'spec_version': str,
            'source': str,
            'correlation_id': str,
            'type': str,
            'data': GatewayEventData
        }

        self.attribute_map = {
            'id': 'id',
            'time': 'time',
            'data_content_type': 'dataContentType',
            'spec_version': 'specVersion',
            'source': 'source',
            'correlation_id': 'correlationID',
            'type': 'type',
            'data': 'data'
        }

        self._id = id
        self._time = time
        self._data_content_type = data_content_type
        self._spec_version = spec_version
        self._source = source
        self._correlation_id = correlation_id
        self._type = type
        self._data = data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GatewayOfflineEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GatewayOfflineEvent of this GatewayOfflineEvent.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this GatewayOfflineEvent.


        :return: The id of this GatewayOfflineEvent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GatewayOfflineEvent.


        :param id: The id of this GatewayOfflineEvent.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def time(self):
        """Gets the time of this GatewayOfflineEvent.

        Time when the event has occurred in RFC3339 format.

        :return: The time of this GatewayOfflineEvent.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this GatewayOfflineEvent.

        Time when the event has occurred in RFC3339 format.

        :param time: The time of this GatewayOfflineEvent.
        :type time: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")

        self._time = time

    @property
    def data_content_type(self):
        """Gets the data_content_type of this GatewayOfflineEvent.

        Content-Type indicating how to parse the `data` attribute. Only 'application/json' is supported for now. If ommitted, it is guaranteed to be `application/json`.

        :return: The data_content_type of this GatewayOfflineEvent.
        :rtype: str
        """
        return self._data_content_type

    @data_content_type.setter
    def data_content_type(self, data_content_type):
        """Sets the data_content_type of this GatewayOfflineEvent.

        Content-Type indicating how to parse the `data` attribute. Only 'application/json' is supported for now. If ommitted, it is guaranteed to be `application/json`.

        :param data_content_type: The data_content_type of this GatewayOfflineEvent.
        :type data_content_type: str
        """
        allowed_values = ["application/json"]  # noqa: E501
        if data_content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `data_content_type` ({0}), must be one of {1}"
                .format(data_content_type, allowed_values)
            )

        self._data_content_type = data_content_type

    @property
    def spec_version(self):
        """Gets the spec_version of this GatewayOfflineEvent.

        The CloudEvents specification that is followed, currently \"1.0\". Only consists of major and minor version parts, to allow patching in a backward-compatible fashion.

        :return: The spec_version of this GatewayOfflineEvent.
        :rtype: str
        """
        return self._spec_version

    @spec_version.setter
    def spec_version(self, spec_version):
        """Sets the spec_version of this GatewayOfflineEvent.

        The CloudEvents specification that is followed, currently \"1.0\". Only consists of major and minor version parts, to allow patching in a backward-compatible fashion.

        :param spec_version: The spec_version of this GatewayOfflineEvent.
        :type spec_version: str
        """
        if spec_version is None:
            raise ValueError("Invalid value for `spec_version`, must not be `None`")

        self._spec_version = spec_version

    @property
    def source(self):
        """Gets the source of this GatewayOfflineEvent.

        Source of the event, which is usually a resource identifier path that can be used to identify the object which triggered the event.

        :return: The source of this GatewayOfflineEvent.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this GatewayOfflineEvent.

        Source of the event, which is usually a resource identifier path that can be used to identify the object which triggered the event.

        :param source: The source of this GatewayOfflineEvent.
        :type source: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    @property
    def correlation_id(self):
        """Gets the correlation_id of this GatewayOfflineEvent.

        ID to identify the request triggering the event.

        :return: The correlation_id of this GatewayOfflineEvent.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this GatewayOfflineEvent.

        ID to identify the request triggering the event.

        :param correlation_id: The correlation_id of this GatewayOfflineEvent.
        :type correlation_id: str
        """

        self._correlation_id = correlation_id

    @property
    def type(self):
        """Gets the type of this GatewayOfflineEvent.

        Type of the event, can be used to determine how the `data` payload is deserialized.

        :return: The type of this GatewayOfflineEvent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GatewayOfflineEvent.

        Type of the event, can be used to determine how the `data` payload is deserialized.

        :param type: The type of this GatewayOfflineEvent.
        :type type: str
        """
        allowed_values = ["gateway/offline"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def data(self):
        """Gets the data of this GatewayOfflineEvent.


        :return: The data of this GatewayOfflineEvent.
        :rtype: GatewayEventData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GatewayOfflineEvent.


        :param data: The data of this GatewayOfflineEvent.
        :type data: GatewayEventData
        """

        self._data = data
