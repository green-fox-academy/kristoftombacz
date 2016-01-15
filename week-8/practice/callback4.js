'use strict';
var fs = require('fs')

function readAlmaTxt(callback) {
  fs.readFile('alma.txt', function(err, content) {
    var out = String(content);
    callback(out);
  });
}

readAlmaTxt(function (content) {
  console.log(content);
});
