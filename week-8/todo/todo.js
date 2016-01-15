'use strict';

function createRequest(url, callback) {

  var probaRequest = new XMLHttpRequest();
  probaRequest.open('GET', url);
  probaRequest.send('');
  probaRequest.onreadystatechange = function () {
    console.log('state: ', probaRequest.readyState);
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}

function postRequest(url, data) {
  var probaRequest2 = new XMLHttpRequest();
  probaRequest2.open('POST', url);
  probaRequest2.setRequestHeader('Content-Type', 'application/json');
  probaRequest2.send(data);
}

var url = "https://mysterious-dusk-8248.herokuapp.com/todos";
var todoContainer = document.querySelector('.todo-container');

function dataToSend(){
  return JSON.stringify({text: 'https://41.media.tumblr.com/60f3122d1d3cfd85cf6edbe509ea89c6/tumblr_mrcxq51Son1qgwqw9o1_500.png'});
}

var todoCallback = function (response) {
  console.log(JSON.parse(response));
  var todoArray = JSON.parse(response);

  todoArray.forEach(function(todoItem) {
    console.log(todoItem.text);
    var newTodoItem = document.createElement('p');
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
  })
}

postRequest(url, dataToSend);
createRequest(url, todoCallback);
