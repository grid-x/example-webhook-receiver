# coding: utf-8

# flake8: noqa
"""
    Webhook Event Receiver API

    This API describes the event webhook calling convention. In order to receive webhook events from the gridX API, third parties must implement endpoints according to this specification. In the following, the external partner API is referred to as  \"external API\", while the gridX API is called \"gridX\". 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openapi_client.models.appliance_event_data import ApplianceEventData
from openapi_client.models.commissioning_data import CommissioningData
from openapi_client.models.ev_event_data import EVEventData
from openapi_client.models.event import Event
from openapi_client.models.event_data import EventData
from openapi_client.models.gateway_event_data import GatewayEventData
from openapi_client.models.inverter_event_data import InverterEventData
from openapi_client.models.notification import Notification
from openapi_client.models.notification_message import NotificationMessage
from openapi_client.models.notification_recipient import NotificationRecipient
