"use-strict";

var TodoItem = function () {
  this.id = nextId();
  this.text = "";
  this.completed = false;
}

var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'test',
  password: 'gyuri',
  database: 'todo'
});

connection.connect();

TodoItem.prototype.update = function(attributes) {
  this.text = attributes.text || "";
  this.completed = !!attributes.completed;
};

var currId = 0;

function nextId() {
  return ++currId;
}

var items = {};

function getItem(id, callback) {
  connection.query('SELECT text,status FROM todo WHERE todo_id=?', id, function(err, result) {
    if (err) {throw err;}
    console.log(result);
    callback(result);
  });
}

function addItem(attributes) {
  connection.query('INSERT INTO todo SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertID);
  })
}

function removeItem(id, callback) {
  connection.query('DELETE FROM todo WHERE todo_id= ?', id, function(err, result){
    if (err) throw err;
    console.log(result.insertId);
    callback(result);
  });
}

function allItems(callback) {
  connection.query('SELECT todo_id,text,status FROM todo;', function(err, result){
    if (err) throw err;
    console.log(result);
    callback(result);
  });
}

function deleteAllItems(callback) {
  connection.query('DELETE * FROM todo;', function(err, result) {
  if (err) throw err;
  callback(results);
  });
}

module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems,
  deleteAll: deleteAllItems
};
