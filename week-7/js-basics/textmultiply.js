'use strict';

function textMultplier(name, multiplier) {
  var finalString = '';
  for (var i = 0; i < multiplier; i++){
    finalString += name;
  }
  return finalString;
}
console.log(textMultplier('cica', 3));
