'use strict';

function createRequest(url, callback) {

  var probaRequest = new XMLHttpRequest();
  probaRequest.open('GET', url);
//  probaRequest.setRequestHeader('X-Mashape-Key', ACCESS_TOKEN);
  probaRequest.send();
  probaRequest.onreadystatechange = function () {
    console.log('state: ', probaRequest.readyState);
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}

var url = "https://mysterious-dusk-8248.herokuapp.com/todos";
var todoCallback = function (response) {
  console.log(JSON.parse(response));
}

createRequest(url, todoCallback);
