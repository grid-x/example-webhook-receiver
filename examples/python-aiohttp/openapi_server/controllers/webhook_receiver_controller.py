from typing import List, Dict
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
from openapi_server import util


async def events_appliance_create_post(request: web.Request, body) -> web.Response:
    """Webhook Receiver

    Called by the gridX API when an appliance is created.

    :param x_signature: The value of this header can be used to authenticate the event payload and is in the format &#x60;&lt;method&gt;&#x3D;&lt;signature&gt;&#x60;. - &#x60;method&#x60; must be \&quot;sha512\&quot; in any case. - &#x60;signature&#x60; is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution 
    :type x_signature: str
    :param body: The event&#39;s payload, partly depending on the event&#39;s type (see parameter eventType).
    :type body: dict | bytes

    """
    body = ApplianceCreateEvent.from_dict(body)
    return web.Response(status=200)


async def events_appliance_offline_post(request: web.Request, body) -> web.Response:
    """Webhook Receiver

    Called by the gridX API when when an appliance goes offline.

    :param x_signature: The value of this header can be used to authenticate the event payload and is in the format &#x60;&lt;method&gt;&#x3D;&lt;signature&gt;&#x60;. - &#x60;method&#x60; must be \&quot;sha512\&quot; in any case. - &#x60;signature&#x60; is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution 
    :type x_signature: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApplianceOfflineEvent.from_dict(body)
    return web.Response(status=200)


async def events_appliance_online_post(request: web.Request, body) -> web.Response:
    """Webhook Receiver

    Called by the gridX API when an appliance comes online.

    :param x_signature: The value of this header can be used to authenticate the event payload and is in the format &#x60;&lt;method&gt;&#x3D;&lt;signature&gt;&#x60;. - &#x60;method&#x60; must be \&quot;sha512\&quot; in any case. - &#x60;signature&#x60; is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution 
    :type x_signature: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApplianceOnlineEvent.from_dict(body)
    print(f"Appliance '{body.data.model}' within the system '{body.data.system_name}' went online")
    print(f'(X-Signature Header {request.headers["x-signature"]})')
    return web.Response(status=200)


async def events_comissioning_done_post(request: web.Request, body) -> web.Response:
    """Webhook Receiver

    Called by the gridX API when commissioning a gateway was finished.

    :param x_signature: The value of this header can be used to authenticate the event payload and is in the format &#x60;&lt;method&gt;&#x3D;&lt;signature&gt;&#x60;. - &#x60;method&#x60; must be \&quot;sha512\&quot; in any case. - &#x60;signature&#x60; is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution 
    :type x_signature: str
    :param body: 
    :type body: dict | bytes

    """
    body = ComissioningDoneEvent.from_dict(body)
    return web.Response(status=200)


async def events_ev_plugged_post(request: web.Request, body) -> web.Response:
    """Webhook Receiver

    Called by the gridX API when an EV charging state changes.

    :param x_signature: The value of this header can be used to authenticate the event payload and is in the format &#x60;&lt;method&gt;&#x3D;&lt;signature&gt;&#x60;. - &#x60;method&#x60; must be \&quot;sha512\&quot; in any case. - &#x60;signature&#x60; is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution 
    :type x_signature: str
    :param body: 
    :type body: dict | bytes

    """
    body = EVPluggedEvent.from_dict(body)
    return web.Response(status=200)


async def events_gateway_create_post(request: web.Request, body) -> web.Response:
    """Webhook Receiver

    Called by the gridX API when a gateway is created.

    :param x_signature: The value of this header can be used to authenticate the event payload and is in the format &#x60;&lt;method&gt;&#x3D;&lt;signature&gt;&#x60;. - &#x60;method&#x60; must be \&quot;sha512\&quot; in any case. - &#x60;signature&#x60; is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution 
    :type x_signature: str
    :param body: 
    :type body: dict | bytes

    """
    body = GatewayCreateEvent.from_dict(body)
    return web.Response(status=200)


async def events_gateway_offline_post(request: web.Request, body) -> web.Response:
    """Webhook Receiver

    Called by the gridX API when a gateway goes offline.

    :param x_signature: The value of this header can be used to authenticate the event payload and is in the format &#x60;&lt;method&gt;&#x3D;&lt;signature&gt;&#x60;. - &#x60;method&#x60; must be \&quot;sha512\&quot; in any case. - &#x60;signature&#x60; is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution 
    :type x_signature: str
    :param body: 
    :type body: dict | bytes

    """
    body = GatewayOfflineEvent.from_dict(body)
    return web.Response(status=200)


async def events_gateway_online_post(request: web.Request, body) -> web.Response:
    """Webhook Receiver

    Called by the gridX API when a gateway comes online.

    :param x_signature: The value of this header can be used to authenticate the event payload and is in the format &#x60;&lt;method&gt;&#x3D;&lt;signature&gt;&#x60;. - &#x60;method&#x60; must be \&quot;sha512\&quot; in any case. - &#x60;signature&#x60; is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution 
    :type x_signature: str
    :param body: 
    :type body: dict | bytes

    """
    body = GatewayOnlineEvent.from_dict(body)
    return web.Response(status=200)


async def events_inverter_status_post(request: web.Request, body) -> web.Response:
    """Webhook Receiver

    Called by the gridX API when an inverter&#39;s status changes.

    :param x_signature: The value of this header can be used to authenticate the event payload and is in the format &#x60;&lt;method&gt;&#x3D;&lt;signature&gt;&#x60;. - &#x60;method&#x60; must be \&quot;sha512\&quot; in any case. - &#x60;signature&#x60; is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution 
    :type x_signature: str
    :param body: 
    :type body: dict | bytes

    """
    body = InverterStatusEvent.from_dict(body)
    return web.Response(status=200)
