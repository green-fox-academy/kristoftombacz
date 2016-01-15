'use strict';

var addItem = document.querySelector('.add-item');

addItem.addEventListener('click', function () {
  var textInput = document.querySelector('.todo-input').value;

  todoStatus.innerText = "";
  var newStatusItem = document.createElement('p');
  var statusLog = textInput + " added to the list."
  newStatusItem.innerText = statusLog;
  todoStatus.appendChild(newStatusItem);

  var newTodo = JSON.stringify({text: textInput});
  createRequest('POST', url, newTodo, listCallback);
  refresh();
})
