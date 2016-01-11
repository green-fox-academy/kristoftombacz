'use strict';

function greet(name) {
  console.log('csa ' + name + '!');
}

greet('gyuri');

var koszontes = greet;
koszontes('ez is gyuri');

var print = console.log('fucku');
print;

var add = function add(a, b){
  return a + b;
}

console.log(add(1,2))

function custom(text) {
  console.log(text, ' valamivalvamivmiav');
}

greet('gyurko', custom('text'))
