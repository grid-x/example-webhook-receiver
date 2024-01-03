from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class EVEventData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, appliance_id=None, gateway_id=None, model=None, manufacturer=None, type=None, kind=None, name=None, serial_number=None, system_id=None, system_name=None, evse_id=None, state=None):  # noqa: E501
        """EVEventData - a model defined in OpenAPI

        :param appliance_id: The appliance_id of this EVEventData.  # noqa: E501
        :type appliance_id: str
        :param gateway_id: The gateway_id of this EVEventData.  # noqa: E501
        :type gateway_id: str
        :param model: The model of this EVEventData.  # noqa: E501
        :type model: str
        :param manufacturer: The manufacturer of this EVEventData.  # noqa: E501
        :type manufacturer: str
        :param type: The type of this EVEventData.  # noqa: E501
        :type type: str
        :param kind: The kind of this EVEventData.  # noqa: E501
        :type kind: str
        :param name: The name of this EVEventData.  # noqa: E501
        :type name: str
        :param serial_number: The serial_number of this EVEventData.  # noqa: E501
        :type serial_number: str
        :param system_id: The system_id of this EVEventData.  # noqa: E501
        :type system_id: str
        :param system_name: The system_name of this EVEventData.  # noqa: E501
        :type system_name: str
        :param evse_id: The evse_id of this EVEventData.  # noqa: E501
        :type evse_id: str
        :param state: The state of this EVEventData.  # noqa: E501
        :type state: str
        """
        self.openapi_types = {
            'appliance_id': str,
            'gateway_id': str,
            'model': str,
            'manufacturer': str,
            'type': str,
            'kind': str,
            'name': str,
            'serial_number': str,
            'system_id': str,
            'system_name': str,
            'evse_id': str,
            'state': str
        }

        self.attribute_map = {
            'appliance_id': 'applianceID',
            'gateway_id': 'gatewayID',
            'model': 'model',
            'manufacturer': 'manufacturer',
            'type': 'type',
            'kind': 'kind',
            'name': 'name',
            'serial_number': 'serialNumber',
            'system_id': 'systemID',
            'system_name': 'systemName',
            'evse_id': 'evseID',
            'state': 'state'
        }

        self._appliance_id = appliance_id
        self._gateway_id = gateway_id
        self._model = model
        self._manufacturer = manufacturer
        self._type = type
        self._kind = kind
        self._name = name
        self._serial_number = serial_number
        self._system_id = system_id
        self._system_name = system_name
        self._evse_id = evse_id
        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'EVEventData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EVEventData of this EVEventData.  # noqa: E501
        :rtype: EVEventData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def appliance_id(self) -> str:
        """Gets the appliance_id of this EVEventData.

        ID of the appliance that caused this event.  # noqa: E501

        :return: The appliance_id of this EVEventData.
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id: str):
        """Sets the appliance_id of this EVEventData.

        ID of the appliance that caused this event.  # noqa: E501

        :param appliance_id: The appliance_id of this EVEventData.
        :type appliance_id: str
        """
        if appliance_id is None:
            raise ValueError("Invalid value for `appliance_id`, must not be `None`")  # noqa: E501

        self._appliance_id = appliance_id

    @property
    def gateway_id(self) -> str:
        """Gets the gateway_id of this EVEventData.

        The ID of the gateway that connects to the appliance.  # noqa: E501

        :return: The gateway_id of this EVEventData.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id: str):
        """Sets the gateway_id of this EVEventData.

        The ID of the gateway that connects to the appliance.  # noqa: E501

        :param gateway_id: The gateway_id of this EVEventData.
        :type gateway_id: str
        """
        if gateway_id is None:
            raise ValueError("Invalid value for `gateway_id`, must not be `None`")  # noqa: E501

        self._gateway_id = gateway_id

    @property
    def model(self) -> str:
        """Gets the model of this EVEventData.

        Model description of the appliance.  # noqa: E501

        :return: The model of this EVEventData.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this EVEventData.

        Model description of the appliance.  # noqa: E501

        :param model: The model of this EVEventData.
        :type model: str
        """

        self._model = model

    @property
    def manufacturer(self) -> str:
        """Gets the manufacturer of this EVEventData.

        Manufacturer of the appliance.  # noqa: E501

        :return: The manufacturer of this EVEventData.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        """Sets the manufacturer of this EVEventData.

        Manufacturer of the appliance.  # noqa: E501

        :param manufacturer: The manufacturer of this EVEventData.
        :type manufacturer: str
        """

        self._manufacturer = manufacturer

    @property
    def type(self) -> str:
        """Gets the type of this EVEventData.

        General type of the appliance.  # noqa: E501

        :return: The type of this EVEventData.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this EVEventData.

        General type of the appliance.  # noqa: E501

        :param type: The type of this EVEventData.
        :type type: str
        """
        allowed_values = ["UNKNOWN", "INVERTER", "METER", "EVSTATION", "HEAT_PUMP", "HEATER", "CONTAINER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def kind(self) -> str:
        """Gets the kind of this EVEventData.

        Kind of the appliance is used to provide further details on the appliance configuration and mode of operation. The kind property is only available for appliances with type INVERTER or METER. For inverters, only UNKNOWN, PV, BATTERY, HYBRID and PV_EXTERNAL are valid values. They describe the  kind of connected appliance(s) and define the role of the inverter in the system. For meters, kind specifies the appliance the meter is attached to. It resembles the location the meter is installed in.   # noqa: E501

        :return: The kind of this EVEventData.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this EVEventData.

        Kind of the appliance is used to provide further details on the appliance configuration and mode of operation. The kind property is only available for appliances with type INVERTER or METER. For inverters, only UNKNOWN, PV, BATTERY, HYBRID and PV_EXTERNAL are valid values. They describe the  kind of connected appliance(s) and define the role of the inverter in the system. For meters, kind specifies the appliance the meter is attached to. It resembles the location the meter is installed in.   # noqa: E501

        :param kind: The kind of this EVEventData.
        :type kind: str
        """
        allowed_values = ["UNKNOWN", "PV", "BATTERY", "HYBRID", "PV_EXTERNAL", "GRID", "HEAT_PUMP", "FUEL_CELL", "HEAT_PUMP_EXTERNAL", "EVSTATION", "BTTP", "HEATING", "MISC", "CLUSTER", "WIND_TURBINE"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def name(self) -> str:
        """Gets the name of this EVEventData.

        The name of the appliance as defined by the customer.  # noqa: E501

        :return: The name of this EVEventData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this EVEventData.

        The name of the appliance as defined by the customer.  # noqa: E501

        :param name: The name of this EVEventData.
        :type name: str
        """

        self._name = name

    @property
    def serial_number(self) -> str:
        """Gets the serial_number of this EVEventData.

        Serial number of the appliance as returned by the appliance.  # noqa: E501

        :return: The serial_number of this EVEventData.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number: str):
        """Sets the serial_number of this EVEventData.

        Serial number of the appliance as returned by the appliance.  # noqa: E501

        :param serial_number: The serial_number of this EVEventData.
        :type serial_number: str
        """

        self._serial_number = serial_number

    @property
    def system_id(self) -> str:
        """Gets the system_id of this EVEventData.

        The ID of the system that the gateway and appliance run in.  # noqa: E501

        :return: The system_id of this EVEventData.
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id: str):
        """Sets the system_id of this EVEventData.

        The ID of the system that the gateway and appliance run in.  # noqa: E501

        :param system_id: The system_id of this EVEventData.
        :type system_id: str
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

    @property
    def system_name(self) -> str:
        """Gets the system_name of this EVEventData.

        Name of the system as defined by the customer.  # noqa: E501

        :return: The system_name of this EVEventData.
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name: str):
        """Sets the system_name of this EVEventData.

        Name of the system as defined by the customer.  # noqa: E501

        :param system_name: The system_name of this EVEventData.
        :type system_name: str
        """

        self._system_name = system_name

    @property
    def evse_id(self) -> str:
        """Gets the evse_id of this EVEventData.

        Electirc Vehicle Supply Equipment ID  # noqa: E501

        :return: The evse_id of this EVEventData.
        :rtype: str
        """
        return self._evse_id

    @evse_id.setter
    def evse_id(self, evse_id: str):
        """Sets the evse_id of this EVEventData.

        Electirc Vehicle Supply Equipment ID  # noqa: E501

        :param evse_id: The evse_id of this EVEventData.
        :type evse_id: str
        """

        self._evse_id = evse_id

    @property
    def state(self) -> str:
        """Gets the state of this EVEventData.

        State of the EV charging station.  # noqa: E501

        :return: The state of this EVEventData.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this EVEventData.

        State of the EV charging station.  # noqa: E501

        :param state: The state of this EVEventData.
        :type state: str
        """
        allowed_values = ["plugged"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state
