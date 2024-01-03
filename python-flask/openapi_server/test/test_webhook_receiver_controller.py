import unittest

from flask import json

from openapi_server.models.event import Event  # noqa: E501
from openapi_server.test import BaseTestCase


class TestWebhookReceiverController(BaseTestCase):
    """WebhookReceiverController integration test stubs"""

    def test_events_event_type_post(self):
        """Test case for events_event_type_post

        Webhook Receiver
        """
        event = {"notification":{"recipient":{"accountID":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","fullName":"fullName","locale":"fr_FR","userID":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","email":"email"},"message":{"textContentType":"text/html","actionURL":"http://example.com/aeiou","text":"text","title":""}},"specVersion":"1.0","data":null,"correlationID":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","time":"2000-01-23T04:56:07.000+00:00","source":"/systems/5eda17ec-4dc9-46d5-b3b8-c396f75a760f","type":"appliance/create","dataContentType":"application/json"}
        headers = { 
            'Content-Type': 'application/json',
            'x_signature': 'sha512=<signature>',
        }
        response = self.client.open(
            '/gridx/events/{event_type}'.format(event_type='appliance/create'),
            method='POST',
            headers=headers,
            data=json.dumps(event),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
