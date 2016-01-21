'use strict';

var refreshList = document.querySelector('.refresh-list');

refreshList.addEventListener('click', function () {

  todoStatus.innerText = "";
  var newStatusItem = document.createElement('p');
  var statusLog = "List refreshed."
  newStatusItem.innerText = statusLog;
  todoStatus.appendChild(newStatusItem);

  refresh();
})
