import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.event import Event  # noqa: E501
from openapi_server import util


def events_event_type_post(event_type, x_signature, event):  # noqa: E501
    """Webhook Receiver

    Called by the gridX API when delivering a webhook. Third parties should use this reference to implement an HTTP handler capable of handling incoming webhooks.   # noqa: E501

    :param event_type: The type of an event (e.g. &#39;appliance/offline&#39;). The path depends on how the webhook has been configured and is not a hard requirement.
    :type event_type: str
    :param x_signature: The value of this header can be used to authenticate the event payload and is in the format &#x60;&lt;method&gt;&#x3D;&lt;signature&gt;&#x60;. - &#x60;method&#x60; must be \&quot;sha512\&quot; in any case. - &#x60;signature&#x60; is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution 
    :type x_signature: str
    :param event: The event&#39;s payload, partly depending on the event&#39;s type (see parameter eventType).
    :type event: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        event = Event.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
