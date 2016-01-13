'use strict';


function createRequest(url, callback) {
    var probaRequest = new XMLHttpRequest();
    probaRequest.open('POST', url);
    probaRequest.setRequestHeader('Content-Type', 'application/json')
    var todo = 'A Guryi nagyon ugyes!';
    probaRequest.send(JSON.stringify({text: todo}));
    probaRequest.onreadystatechange = function() {
        if (probaRequest.readyState === 4) {
            callback(probaRequest.response);
        }
    }
};

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos'
var todoContainer = document.querySelector('.todo-container');

function todoCallback(response) {
    var todoItem = JSON.parse(response);
    var newTodoItem = document.createElement('p');
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem)
}

createRequest(url, todoCallback);




