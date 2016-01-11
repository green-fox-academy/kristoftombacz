'use strict';

var sum = function (array) {
  var sumArray = 0;

  for (var i = 0; i < array.length; i++) {
    sumArray += array[i]
  }
  return sumArray;
}

console.log(sum([5, 10, 15, 6]));
