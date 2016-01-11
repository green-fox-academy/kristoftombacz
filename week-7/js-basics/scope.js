'use strict';

var g = 123;

function printG() {
  console.log(g)
  g = 333;
}

printG()
console.log(g)
