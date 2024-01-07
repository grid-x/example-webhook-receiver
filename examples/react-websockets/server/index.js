const express = require("express");
const ws = require("ws");
const app = express();

const wss = new ws.WebSocketServer({ port: 8088 });
wss.on("connection", function connection(ws) {
  console.log("WebSocket client connected");
  ws.on("error", console.error);
});

app.use(express.json());
app.listen(8080, () => {
  console.log("Server started");
});

const relayEvent = (data) => {
  wss.clients.forEach(function each(client) {
    if (client.readyState === ws.WebSocket.OPEN) {
      client.send(JSON.stringify(data));
    }
  });
};

const metadataFromEvent = (eventPayload) =>
  ({ gatewayID, applianceID, systemName, model } = eventPayload);

app.post("/gridx/events/appliance/online", (req, res) =>
  relayEvent({
    ...metadataFromEvent(req.body.data),
    online: true,
  })
);

app.post("/gridx/events/appliance/offline", (req, res) =>
  relayEvent({
    ...metadataFromEvent(req.body.data),
    online: false,
  })
);
