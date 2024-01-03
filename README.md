# :spider_web: :hook: Example gridX Webhook Receivers

`Webhook Receivers` are used to get notifications about state changes in gridX/XENON within your app.
A webhook receiver is a publicly accessible endpoint on a server that is called by gridX when domain events, e.g., when an appliance goes online, occur.
By implementing a webhook receiver, you can react on these events within your custom application.
This allows for push based delivery of events as opposed to your app having to pull gridX's API constantly.

If you want to learn more, [GitHub has a nice intro about webhooks](https://docs.github.com/en/webhooks/about-webhooks).

This repository contains sample webhook receiver implementations and instructions on how to generate receivers in a plethora of languages/frameworks to get you started.

## :toolbox: Prerequisites

* [for local development] [`ngrok`](https://ngrok.com/) to expose the locally running webhook receiver to the internet. You need to [sign up](https://ngrok.com/signup) for a free `ngrok` account and [connect it](https://dashboard.ngrok.com/get-started/setup/macos) to be able to use it.
* [for server scaffold generation] [`openapi-generator`](https://openapi-generator.tech/) can be used to generate server stubs for different languages.

## :bookmark_tabs: Usage

### :incoming_envelope: Receiving Events from gridX

To be able to receive events from gridX, you need to ...

1. ... run a webhook receiver from either of the samples below
2. ... expose the server to the internet using `ngrok`
3. ... configure a webhook rule in XENON
4. ... remove the webhook rule after you're done with testing

#### 1. Run a sample webhook receiver

Pick one of the samples below to run and start the server according to the corresponding README.

The NodeJS server, e.g., can be started like this.

```sh
cd examples/node-express
yarn
yarn start
```

You can test whether any of the example receivers is running by just posting an empty JSON against `localhost:8080/gridx/events/appliance/online`. You'll likely get an error message (depending on the sample), but can see that a connection was made.

```sh
curl -X POST localhost:8080/gridx/events/appliance/online -d '{}'
```

#### 2. Expose the Server to the internet

All sample servers will start on port `:8080`. Run one of the examples below as described in the corresponding README and set up routing through ngrok: `ngrok http 8080`

This will set up a publicly accessible tunnel to the server running locally and show you the target URL required in the next step.

After setting up the `ngrok` tunnel, you can use the [local ngrok console](http://127.0.0.1:4040/inspect/http) to inspect incoming events.

#### 3. Configure Webhook Rule

To be able to receive events, you first need to register a notification rule through the API for the events you wish to receive.

You need the following data to call the API:

* The account id for which you want to receive event notifications (from XENON account details page)
* The user id for which you want to receive event notifications (from your user details page on XENON). This is typically an administrative user for the resp. account
* Your API token (from your XENON user settings)
* The external webhook receiver URL. During development, this will be the external `ngrok` URL.
* The event type you want to receive. Available event types are:
  * appliance/create
  * appliance/offline
  * appliance/online
  * inverter/status
  * gateway/create
  * gateway/offline
  * gateway/online
  * ev/plugged
  * commissioning/done

_register-appliance-online-webhook.json_
```json
{
    "eventType": "appliance/online",
    "notificationType": {
        "webhook": {
        "targetURL": "<webhook receiver URL>"
      }
    }
}
```

```sh
curl https://api.gridx.de/accounts/<your account id>/users/<your user id>/notifications/rules \
  --header 'authorization: Bearer <your API token>' \
  --header 'accept: application/vnd.gridx.v2+json' \
  --header 'content-type: application/json' \
  --data @register-appliance-online-webhook.json
```

To verify your rule was created, you can retrieve the current rules from the API. Please note the `id` property of the rule you just created.

```sh
curl https://api.gridx.de/accounts/<your account id>/users/<your user id>/notifications/rules \
  --header 'authorization: Bearer <your API token>' \
  --header 'accept: application/vnd.gridx.v2+json' \
  --header 'content-type: application/json'
```


#### 4. Clean up rules created for testing

After testing, please remember to remove the rule again to prevent continuous failures due to failed event deliveries.

```sh
curl -X DELETE \
  https://api.gridx.de/accounts/<your account id>/users/<your user id>/notifications/rules/<rule id> \
  --header 'authorization: Bearer <your API token>' \
  --header 'accept: application/vnd.gridx.v2+json' \
  --header 'content-type: application/json'
```

### :bento: Samples

* [NodeJS/Express](./examples/node-express/README.md): Hand-written webhook receiver that writes the IDs of appliances coming online to the console.
* [Go](./examples/go-server/README.md): Server with stubs for all supported event types generated using `openapi-generator`
* Python/Flask: Server with stubs for all supported event types generated using `openapi-generator`

### :factory: Generating Server Stubs

TODO
