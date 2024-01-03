const express = require("express");
const app = express();

app.use(express.json())

app.post("/gridx/events/appliance/online", (req, res) => {
  const { systemName, model } = req.body.data 
  console.log(`Appliance '${model}' within the system '${systemName}' went online`)
});

app.listen(8080, () => {
  console.log("Server started");
});
