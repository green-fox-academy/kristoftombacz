'use strict';

var url = "http://localhost:3000/todos";
var todoContainer = document.querySelector('.todo-container');
var todoStatus = document.querySelector('.todo-status');

var listCallback = function (response) {
  var todoArray = JSON.parse(response);

  todoContainer.innerHTML = '';
  todoArray.forEach(function(todoItem) {
    var itemText = todoItem.text + "   " ;
    var newTodoItem = document.createElement('p');
    var newImgItem = document.createElement('img');

    newImgItem.setAttribute('src', "img/x.png");
    newTodoItem.setAttribute('id', todoItem.id);
    newImgItem.setAttribute('id', todoItem.id);

    newTodoItem.innerHTML = itemText;
    newTodoItem.appendChild(newImgItem);
    todoContainer.appendChild(newTodoItem);

    newImgItem.addEventListener('click', function(e) {

      todoStatus.innerText = "";
      var newStatusItem = document.createElement('p');
      var statusLog = "1 item deleted from the list.";
      newStatusItem.innerText = statusLog;
      todoStatus.appendChild(newStatusItem);

      console.log(newTodoItem);

      var id = e.target.getAttribute("id");
      createRequest('DELETE', url +'/' + id, undefined, refresh)
    });
  })
}

var refresh = function () {
  createRequest('GET', url, {}, listCallback);
}

refresh();
