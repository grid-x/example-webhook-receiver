import "./App.css";

import { useState, useEffect } from "react";

const socket = new WebSocket("ws://localhost:8088");

// Connect to websocket server
socket.addEventListener("open", (event) => {
  socket.send("Connection established");
});

function App() {
  // Holds the state of all systems and appliances the component has seen events for
  const [systems, setSystems] = useState({});

  // Add websocket listener when the component renders and remove it when it is destroyed.
  useEffect(() => {
    socket.addEventListener("message", consumeMessage);
    return () => socket.removeEventListener("message", consumeMessage);
  });

  // Whenever a message arrives, update the local state (i.e. the systems displayed)
  const consumeMessage = (event) => {
    const payload = JSON.parse(event.data);

    if (systems[payload.gatewayID]) {
      const appliances = systems[payload.gatewayID].appliances;
      appliances[payload.applianceID] = payload;
      systems.appliances = appliances;
    } else {
      systems[payload.gatewayID] = {
        gatewayID: payload.gatewayID,
        systemName: payload.systemName,
        appliances: {
          [payload.applianceID]: payload,
        },
      };
    }

    setSystems({ ...systems });
  };

  return (
    <div className="App">
      <div className="systems">
        {systems &&
          Object.values(systems).map(
            (system) =>
              system.gatewayID && (
                <System system={system} key={system.gatewayID} />
              )
          )}
      </div>
    </div>
  );
}

const System = ({ system }) => (
  <div className="system" id={system.gatewayID}>
    <div className="systemName">{system.systemName}</div>
    <div className="appliances">
      {system.appliances &&
        Object.values(system.appliances)?.map((appliance) => (
          <Appliance appliance={appliance} key={appliance.applianceID} />
        ))}
    </div>
  </div>
);

const Appliance = ({ appliance }) => (
  <div
    id={appliance.applianceID}
    className={`appliance ${appliance.online ? "online" : "offline"}`}
  >
    {appliance.manufacturer}
    <br />
    {appliance.model}
  </div>
);

export default App;
