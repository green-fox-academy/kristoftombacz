'use strict';

var fs = require('fs');

function getFirstIndexInAlmaTxt(letter, callback) {

  fs.readFile('almsada.txt', function(err, content) {
    if (err) {
      return callback(err);
    }

    var output = String(content);
    for (var i = 0; i < output.length; i++) {
      if (output[i] === letter) {
        return callback(i);
      }
    }
  })
}

getFirstIndexInAlmaTxt('a', function(index) {
  console.log(index); // 3
})
