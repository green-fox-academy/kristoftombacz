'use strict';

var fs = require('fs');
function countLetterP(callback) {
  fs.readFile('alma.txt', function(err, content) {
    var out = String(content);
    var count = 0;
    for (var i = 0; i < content.length; i++){
      if (out[i] === 'p'){
        count++;
      }
    }
    callback(count);
  });
}

countLetterP(function(count) {
  console.log(count); // 2
});
