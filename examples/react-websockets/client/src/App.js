import "./App.css";

import { useState, useEffect } from "react";

const socket = new WebSocket("ws://localhost:8088");

socket.addEventListener("open", (event) => {
  socket.send("Connection established");
});

function App() {
  const [systems, setSystems] = useState({});

  useEffect(() => {
    socket.addEventListener("message", consumeMessage);
    return () => socket.removeEventListener("message", consumeMessage);
  });

  const consumeMessage = (event) => {
    const payload = JSON.parse(event.data);

    if (systems[payload.gatewayID]) {
      systems[payload.gatewayID].appliances = [...systems[payload.gatewayID].appliances, payload];
    } else {
      systems[payload.gatewayID] = {
        gatewayID: payload.gatewayID,
        systemName: payload.systemName,
        appliances: [payload],
      };
    }

    setSystems({ ...systems });
  };


  return (
    <div className="App">
      <div className="systems">
        {Object.values(systems).map((system) => (
          <System system={system} key={system.gatewayID}/>
        ))}
      </div>
    </div>
  );
}

const System = ({ system }) => (
  <div className="system">
    <div className="systemName">{system.systemName}</div>
    <div className="appliances">
      {system.appliances?.map((appliance) => (
        <Appliance appliance={appliance} key={appliance.applianceID}/>
      ))}
    </div>
  </div>
);

const Appliance = ({ appliance }) => (
  <div className={`appliance ${appliance.online ? "online" : "offline"}`}>
    {appliance.manufacturer}<br/>{appliance.model}
  </div>
);

export default App;
