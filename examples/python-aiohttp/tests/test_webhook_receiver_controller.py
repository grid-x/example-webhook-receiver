# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.appliance_create_event import ApplianceCreateEvent
from openapi_server.models.appliance_offline_event import ApplianceOfflineEvent
from openapi_server.models.appliance_online_event import ApplianceOnlineEvent
from openapi_server.models.comissioning_done_event import ComissioningDoneEvent
from openapi_server.models.ev_plugged_event import EVPluggedEvent
from openapi_server.models.gateway_create_event import GatewayCreateEvent
from openapi_server.models.gateway_offline_event import GatewayOfflineEvent
from openapi_server.models.gateway_online_event import GatewayOnlineEvent
from openapi_server.models.inverter_status_event import InverterStatusEvent


pytestmark = pytest.mark.asyncio

async def test_events_appliance_create_post(client):
    """Test case for events_appliance_create_post

    Webhook Receiver
    """
    body = null
    headers = { 
        'Content-Type': 'application/json',
        'x_signature': 'sha512=<signature>',
    }
    response = await client.request(
        method='POST',
        path='/gridx/events/appliance/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_appliance_offline_post(client):
    """Test case for events_appliance_offline_post

    Webhook Receiver
    """
    body = null
    headers = { 
        'Content-Type': 'application/json',
        'x_signature': 'sha512=<signature>',
    }
    response = await client.request(
        method='POST',
        path='/gridx/events/appliance/offline',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_appliance_online_post(client):
    """Test case for events_appliance_online_post

    Webhook Receiver
    """
    body = null
    headers = { 
        'Content-Type': 'application/json',
        'x_signature': 'sha512=<signature>',
    }
    response = await client.request(
        method='POST',
        path='/gridx/events/appliance/online',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_comissioning_done_post(client):
    """Test case for events_comissioning_done_post

    Webhook Receiver
    """
    body = null
    headers = { 
        'Content-Type': 'application/json',
        'x_signature': 'sha512=<signature>',
    }
    response = await client.request(
        method='POST',
        path='/gridx/events/comissioning/done',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_ev_plugged_post(client):
    """Test case for events_ev_plugged_post

    Webhook Receiver
    """
    body = null
    headers = { 
        'Content-Type': 'application/json',
        'x_signature': 'sha512=<signature>',
    }
    response = await client.request(
        method='POST',
        path='/gridx/events/ev/plugged',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_gateway_create_post(client):
    """Test case for events_gateway_create_post

    Webhook Receiver
    """
    body = null
    headers = { 
        'Content-Type': 'application/json',
        'x_signature': 'sha512=<signature>',
    }
    response = await client.request(
        method='POST',
        path='/gridx/events/gateway/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_gateway_offline_post(client):
    """Test case for events_gateway_offline_post

    Webhook Receiver
    """
    body = null
    headers = { 
        'Content-Type': 'application/json',
        'x_signature': 'sha512=<signature>',
    }
    response = await client.request(
        method='POST',
        path='/gridx/events/gateway/offline',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_gateway_online_post(client):
    """Test case for events_gateway_online_post

    Webhook Receiver
    """
    body = null
    headers = { 
        'Content-Type': 'application/json',
        'x_signature': 'sha512=<signature>',
    }
    response = await client.request(
        method='POST',
        path='/gridx/events/gateway/online',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_events_inverter_status_post(client):
    """Test case for events_inverter_status_post

    Webhook Receiver
    """
    body = null
    headers = { 
        'Content-Type': 'application/json',
        'x_signature': 'sha512=<signature>',
    }
    response = await client.request(
        method='POST',
        path='/gridx/events/inverter/status',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

