'use strict';

function greet(name) {
  console.log('Hi ' + name + '!');
}

greet('ezanevem');
greet('tojas', 4, 5, 'csakapucsli');
greet();

function double(num) {
  return num * 2;
}
console.log(double(123));
