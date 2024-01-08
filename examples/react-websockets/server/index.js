const express = require("express");
const ws = require("ws");
const app = express();

// Set up web socket server
const wss = new ws.WebSocketServer({ port: 8088 });
wss.on("connection", function connection(ws) {
  console.log("WebSocket client connected");
  ws.on("error", console.error);
});

// Set up http server for receiving webhooks
app.use(express.json());
app.listen(8080, () => {
  console.log("Server started");
});

// Forwards `data` to each connected websocket client.
const relayEvent = (data) => {
  wss.clients.forEach(function each(client) {
    if (client.readyState === ws.WebSocket.OPEN) {
      client.send(JSON.stringify(data));
    }
  });
};

const metadataFromEvent = (eventPayload) =>
  ({ gatewayID, applianceID, systemName, model } = eventPayload);

// In the handler, we relay the event to the websocket clients and set the status.
// This omits verifying the webhook request. Make sure to validate
// the signature when building your own thing, as described in the corresponding sample.
app.post("/gridx/events/appliance/online", (req, res) => 
  relayEvent({
    ...metadataFromEvent(req.body.data),
    online: true,
  })
);

// In the handler, we relay the event to the websocket clients and set the status.
// This omits verifying the webhook request. Make sure to validate
// the signature when building your own thing, as described in the corresponding sample.
app.post("/gridx/events/appliance/offline", (req, res) =>
  relayEvent({
    ...metadataFromEvent(req.body.data),
    online: false,
  })
);
