"use-strict"

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '',
  database : 'todo'
});

connection.connect();

function getAllItems(cb) {
  connection.query('SELECT * FROM `todo`', function(err, res) {
    if (err) throw err;
    cb(res);
  });
}

function addItem(item, cb) {
  connection.query('INSERT INTO todo SET text=?', item, function(err, result) {
    if (err) throw err;
    cb(result)
  });
}

function removeItem(id, cb) {
  connection.query('DELETE FROM `todo` WHERE todo_id=?', id, function(err, results) {
    if (err) throw err;
    cb(results);
  });
}

function updateItem(id, cb) {
  connection.query('UPDATE `todo` SET completed= \'true\' WHERE todo_id=?', id, function(err, results) {
    if (err) throw err;
    cb(results);
  });
}


module.exports = {
  add: addItem,
  remove: removeItem,
  all: getAllItems,
  update: updateItem,
};
