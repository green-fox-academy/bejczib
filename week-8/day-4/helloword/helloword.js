var express = require('express');
var url = require('url');
var app = express()

app.get('/', function (req,res){
  res.send('Hello wold');
});

app.get('/add', function (req, res) {
    var urlParts = url.parse(req.url, true);
    var query = urlParts.query

    var a = parseInt(query['a']);
    var b = parseInt(query['b']);
    var result = a+b;
    res.send(result + '\n');
})

app.post('/add', function (req, res) {
    console.log(req.body);
    req.status(204).end();

});
app.get('/:name', function (req, res) {
    var name = req.params['name'];
    console.log('Name: ' + name)
    res.send('Hello, ' + name + '\n');
})

app.listen(3000);
