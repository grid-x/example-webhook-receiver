const express = require("express");
const app = express();

app.use(express.json())

app.post("/gridx/events/:eventType", (req, res) => {
  console.log(JSON.stringify(req.body, null, 2));
});

app.listen(8080, () => {
  console.log("Server started");
});
