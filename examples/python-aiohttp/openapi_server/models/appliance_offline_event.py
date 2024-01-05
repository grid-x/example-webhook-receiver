# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.appliance_event_data import ApplianceEventData
from openapi_server import util


class ApplianceOfflineEvent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, time: datetime=None, data_content_type: str='application/json', spec_version: str=None, source: str=None, correlation_id: str=None, type: str=None, data: ApplianceEventData=None):
        """ApplianceOfflineEvent - a model defined in OpenAPI

        :param id: The id of this ApplianceOfflineEvent.
        :param time: The time of this ApplianceOfflineEvent.
        :param data_content_type: The data_content_type of this ApplianceOfflineEvent.
        :param spec_version: The spec_version of this ApplianceOfflineEvent.
        :param source: The source of this ApplianceOfflineEvent.
        :param correlation_id: The correlation_id of this ApplianceOfflineEvent.
        :param type: The type of this ApplianceOfflineEvent.
        :param data: The data of this ApplianceOfflineEvent.
        """
        self.openapi_types = {
            'id': str,
            'time': datetime,
            'data_content_type': str,
            'spec_version': str,
            'source': str,
            'correlation_id': str,
            'type': str,
            'data': ApplianceEventData
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
    def from_dict(cls, dikt: dict) -> 'ApplianceOfflineEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ApplianceOfflineEvent of this ApplianceOfflineEvent.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ApplianceOfflineEvent.


        :return: The id of this ApplianceOfflineEvent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplianceOfflineEvent.


        :param id: The id of this ApplianceOfflineEvent.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def time(self):
        """Gets the time of this ApplianceOfflineEvent.

        Time when the event has occurred in RFC3339 format.

        :return: The time of this ApplianceOfflineEvent.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ApplianceOfflineEvent.

        Time when the event has occurred in RFC3339 format.

        :param time: The time of this ApplianceOfflineEvent.
        :type time: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")

        self._time = time

    @property
    def data_content_type(self):
        """Gets the data_content_type of this ApplianceOfflineEvent.

        Content-Type indicating how to parse the `data` attribute. Only 'application/json' is supported for now. If omitted, it is guaranteed to be `application/json`.

        :return: The data_content_type of this ApplianceOfflineEvent.
        :rtype: str
        """
        return self._data_content_type

    @data_content_type.setter
    def data_content_type(self, data_content_type):
        """Sets the data_content_type of this ApplianceOfflineEvent.

        Content-Type indicating how to parse the `data` attribute. Only 'application/json' is supported for now. If omitted, it is guaranteed to be `application/json`.

        :param data_content_type: The data_content_type of this ApplianceOfflineEvent.
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
        """Gets the spec_version of this ApplianceOfflineEvent.

        The CloudEvents specification that is followed, currently \"1.0\". Only consists of major and minor version parts, to allow patching in a backward-compatible fashion.

        :return: The spec_version of this ApplianceOfflineEvent.
        :rtype: str
        """
        return self._spec_version

    @spec_version.setter
    def spec_version(self, spec_version):
        """Sets the spec_version of this ApplianceOfflineEvent.

        The CloudEvents specification that is followed, currently \"1.0\". Only consists of major and minor version parts, to allow patching in a backward-compatible fashion.

        :param spec_version: The spec_version of this ApplianceOfflineEvent.
        :type spec_version: str
        """
        if spec_version is None:
            raise ValueError("Invalid value for `spec_version`, must not be `None`")

        self._spec_version = spec_version

    @property
    def source(self):
        """Gets the source of this ApplianceOfflineEvent.

        Source of the event, which is usually a resource identifier path that can be used to identify the object which triggered the event.

        :return: The source of this ApplianceOfflineEvent.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ApplianceOfflineEvent.

        Source of the event, which is usually a resource identifier path that can be used to identify the object which triggered the event.

        :param source: The source of this ApplianceOfflineEvent.
        :type source: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    @property
    def correlation_id(self):
        """Gets the correlation_id of this ApplianceOfflineEvent.

        ID to identify the request triggering the event.

        :return: The correlation_id of this ApplianceOfflineEvent.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this ApplianceOfflineEvent.

        ID to identify the request triggering the event.

        :param correlation_id: The correlation_id of this ApplianceOfflineEvent.
        :type correlation_id: str
        """

        self._correlation_id = correlation_id

    @property
    def type(self):
        """Gets the type of this ApplianceOfflineEvent.


        :return: The type of this ApplianceOfflineEvent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApplianceOfflineEvent.


        :param type: The type of this ApplianceOfflineEvent.
        :type type: str
        """
        allowed_values = ["appliance/offline"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def data(self):
        """Gets the data of this ApplianceOfflineEvent.


        :return: The data of this ApplianceOfflineEvent.
        :rtype: ApplianceEventData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ApplianceOfflineEvent.


        :param data: The data of this ApplianceOfflineEvent.
        :type data: ApplianceEventData
        """

        self._data = data
