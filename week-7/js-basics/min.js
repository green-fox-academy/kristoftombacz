'use strict';

var numbers = [7, 8, -1, 4, 3, 12];
min = numbers[0];

for (var i = 0; i < numbers.length; i++){
  if (min > numbers[i]) {
    min = numbers[i];
  }
}

console.log(min);
