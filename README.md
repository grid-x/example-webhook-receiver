# :spider_web: :hook: Example gridX Webhook Receivers

`Webhook Receivers` are used to get notifications about state changes in gridX/XENON within your app.
A webhook receiver is a publicly accessible endpoint on a server that is called by gridX when domain events, e.g., when an appliance goes online, occur. 
By implementing a webhook receiver, you can react on these events within your custom application.
This allows for push based delivery of events as opposed to your app having to pull gridX's API constantly.

If you want to learn more, [GitHub has a nice intro](https://docs.github.com/en/webhooks/about-webhooks) on webhooks.


### Prerequisites

* [for local development] [`ngrok`](https://ngrok.com/) to expose the locally running webhook receiver to the internet. You need to [sign up](https://ngrok.com/signup) for a free `ngrok` account and [connect it](https://dashboard.ngrok.com/get-started/setup/macos) to be able to use it.

## Manual Implementation

### Test Server

```sh
curl -X POST localhost:8080/gridx/events/test -d '{}'  
```

Go to the [local ngrok console](http://127.0.0.1:4040/inspect/http) to inspect incoming events.

## Generated Server Scaffolding

### Go

#### Usage

```sh
cd go-server
go run main.go
```

### Python/Flask

  17   │ pip3 install -r requirements.txt
  18   │ python3 -m openapi_server

