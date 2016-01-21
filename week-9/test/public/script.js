'use strict';

var url = 'http://localhost:3000/todos';
var newTodo = document.querySelector('.new-todo');
var addItemButton = document.querySelector('.add-button');
var deleteButton = document.querySelector('.delete-button');
var doneButton = document.querySelector('.done-button');
var todoContainer = document.querySelector('.todo-container');

function createRequest (method, url, data, callback) {
  var todoRequest = new XMLHttpRequest();
  todoRequest.open(method, url);
  todoRequest.setRequestHeader('Content-Type', 'application/json');
  todoRequest.send(data);
  todoRequest.onreadystatechange = function () {
    if (todoRequest.readyState === 4) {
      callback(todoRequest.response);
    }
  };
}


var listCallback = function (response) {
  var todoItems = JSON.parse(response);
  todoContainer.innerHTML = '';
  todoItems.forEach(function(todoItem){
    var newTodoItem = document.createElement('li');
    newTodoItem.innerText = todoItem.text;
    if (todoItem.completed === 'ttrue') {
      newTodoItem.classList.add('done');
    }
    newTodoItem.setAttribute('id', todoItem.todo_id);
    var checkBox = document.createElement('input');
    checkBox.setAttribute('type', 'checkbox');
    checkBox.setAttribute('class', 'checkbox');
    checkBox.setAttribute('id', todoItem.todo_id);
    todoContainer.appendChild(newTodoItem);
    newTodoItem.appendChild(checkBox);
  });
}

function completed() {
    var checkboxes = document.querySelectorAll('.checkbox');
    var p = document.querySelectorAll('li');
    for (var i=0;i<checkboxes.length;i++) {
        if(checkboxes[i].checked === true) {
            var text = p[i].innerText
            var data = JSON.stringify({ 'text': text, 'completed': true });
            createRequest('PUT', url + '/' + parseInt(checkboxes[i].id), data, createTodoCallback;
            }
        }
}


function deleteItem() {
    var checkboxes = document.querySelectorAll('.checkbox');
    for (var i=0;i<checkboxes.length;i++) {
        if(checkboxes[i].checked === true) {
            createRequest('DELETE', url + '/' + parseInt(checkboxes[i].id), undefined, createTodoCallback);
        }
    }
    refresh();
}

var refresh = function () {
  createRequest('GET', url, {}, listCallback);
}

refresh();


var createTodoCallback = function (response) {
  refresh();
}


addItemButton.addEventListener('click', function() {
    var todo = JSON.stringify({text: newTodo.value})
    createRequest('POST', url, todo, createTodoCallback)
    newTodo.value = '';
});

deleteButton.addEventListener('click', function() {
    deleteItem();
});

doneButton.addEventListener('click', function() {
    completed();
});
