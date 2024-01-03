# openapi_client.WebhookReceiverApi

All URIs are relative to *https://external-api/gridx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_event_type_post**](WebhookReceiverApi.md#events_event_type_post) | **POST** /events/{eventType} | Webhook Receiver


# **events_event_type_post**
> events_event_type_post(event_type, x_signature, event)

Webhook Receiver

Called by the gridX API when delivering a webhook. Third parties should use this reference to implement an HTTP handler capable of handling incoming webhooks.  

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.event import Event
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://external-api/gridx
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://external-api/gridx"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.WebhookReceiverApi(api_client)
    event_type = 'appliance/create' # str | The type of an event (e.g. 'appliance/offline'). The path depends on how the webhook has been configured and is not a hard requirement.
    x_signature = 'sha512=<signature>' # str | The value of this header can be used to authenticate the event payload and is in the format `<method>=<signature>`. - `method` must be \"sha512\" in any case. - `signature` is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution 
    event = openapi_client.Event() # Event | The event's payload, partly depending on the event's type (see parameter eventType).

    try:
        # Webhook Receiver
        api_instance.events_event_type_post(event_type, x_signature, event)
    except Exception as e:
        print("Exception when calling WebhookReceiverApi->events_event_type_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | **str**| The type of an event (e.g. &#39;appliance/offline&#39;). The path depends on how the webhook has been configured and is not a hard requirement. | 
 **x_signature** | **str**| The value of this header can be used to authenticate the event payload and is in the format &#x60;&lt;method&gt;&#x3D;&lt;signature&gt;&#x60;. - &#x60;method&#x60; must be \&quot;sha512\&quot; in any case. - &#x60;signature&#x60; is computed using the HMAC algorithm (as described in [RFC2104](https://datatracker.ietf.org/doc/html/rfc2104)) with SHA512 as hash function, with the request body as data and a pre-defined secret as key (that is only known between the external API and gridX). This is the same method as described in the W3C WebSub standard X-Hub-Signature, see: https://www.w3.org/TR/websub/#authenticated-content-distribution  | 
 **event** | [**Event**](Event.md)| The event&#39;s payload, partly depending on the event&#39;s type (see parameter eventType). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully received event (no issue with payload or validation).  |  -  |
**403** | Indicate that signature validation was not successful.  |  -  |
**404** | Not Found - indicate that the external API is not available.  |  -  |
**500** | Indicate that there is a temporary fault on the external API. gridX will do its best to retry delivery in this case.  |  -  |
**503** | Indicate that the service is temporarily unavailable. gridX will do its best to retry delivery in this case.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

