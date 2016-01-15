'use strict';

var express = require('express');
var url = require('url');
var bodyParser = require('body-parser');
var app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }))

app.get('/', function(req, res) {
  res.send('Hello World!');
})

app.get('/add', function(req, res) {
  var urlParts = url.parse(req.url, true);
  var query = urlParts.query;

  var a = parseInt(query['a']);
  var b = parseInt(query['b']);
  var result = a + b;

  res.send(String(result));
})

app.post('/add', function (req, res){

  console.log(req.body);
  res.status(204).end();
})

app.get('/:name', function(req, res) {
  var name = req.params['name'];
  console.log('name: ' + name);

  res.send('hello ' + name + '\n');
})

app.listen(3000);
