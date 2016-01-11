'use strict';

function reverse(string) {
  var result = '';
  for (var i = string.length-1; i >= 0; i--){
    result += string[i];
  }
  return result;
}

console.log(reverse('kacsagec'));

//recursive

function recursiveReverse(string, pos){
  if (pos < 0) {
  return console.log('');
  } else {
    return string[pos] + recursiveReverse(string, pos - 1);
  }
}

console.log(reverse('kacsagec', 4));

function reverse2(string) {
  return recursiveReverse(string, string.length - 1);
}

console.log(reverse2('kacsagec'));
