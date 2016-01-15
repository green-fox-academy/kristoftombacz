'use strict';

var delButton = document.querySelector('.del-item');
var delElement = document.querySelector('.imag');
var deleteUrl;

delButton.addEventListener('click', function (){

  todoStatus.innerText = "";
  var newStatusItem = document.createElement('p');
  var statusLog = "Deleted all items form the list."
  newStatusItem.innerText = statusLog;
  todoStatus.appendChild(newStatusItem);

var todoArray =  document.querySelectorAll('p');
  for (var i = 0; todoArray.length; i++){
    deleteUrl = url + '/' + todoArray[i].id;
    createRequest('DELETE', deleteUrl, undefined, refresh);
  }
})
