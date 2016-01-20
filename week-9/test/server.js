"use strict"

var express = require("express");
var bodyParser = require("body-parser");
var items = require("./items.js");

var app = express();

app.use(express.static("public"));
app.use(bodyParser.json());


app.get("/todos", function (req, res) {
  items.all(function(item) {
    res.json(item);
  });
});

app.post("/todos", function (req, res) {
  items.add(req.body.text, function(item) {
    res.json(item);
  });

});


app.delete("/todos/:id", function (req, res) {
  items.remove(req.params.id, function(item) {
    res.json(item);
  });
});

app.put("/todos/:id", function (req, res) {
  items.update(req.params.id, function(item) {
    res.json(item);
  });
});



var port = parseInt(process.env.PORT || "3000");
app.listen(port, function () {
  console.log("Listening on port 3000...")
});


