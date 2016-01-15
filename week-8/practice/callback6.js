'use strict';

var fs = require('fs');
function countLetterInAlmaTxt(letter, callback){
  var count = 0;
  fs.readFile('alma.txt', function(err, content){
    var output = String(content);
    for (var i = 0; i < output.length; i++){
      if(output[i] === letter){
        count++;
      }
    }
    callback(count);
  });
}

countLetterInAlmaTxt('p', function(count){
  console.log(count); // 1
});
