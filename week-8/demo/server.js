'use srcpit';

var express = require('express');
var bodyParser = require('body-parser');
var app = express()
// var items = require('./items.js')

app.use(bodyParser.json());
app.use(express.static("public"));

app.get('/todos', function(req, res) {
    res.send('hello');
})

app.post('/todos', function(req, res) {
    var id = req.params['id'];
    res.send('hello ' + id);
})

app.get('/todos/:id', function(req, res) {
    var id = req.params['id'];
    res.send('hello ' + id);
})

app.put('/todos/:id', function(req, res) {
    var id = req.params['id'];
    res.send('hello ' + id);
})


app.delete('/todos/:id', function(req, res) {
    var id = req.params['id'];
    res.send('hello ' + id);
})




app.listen(3000);
