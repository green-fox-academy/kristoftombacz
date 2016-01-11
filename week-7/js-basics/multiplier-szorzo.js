'use strict';

var szorzotabla = '';
for (var i = 1; i <= 10; i++){
  szorzotabla += i + ' * ' + 4 + ' = ' + i * 4 + '\n';
}

var szorzotabla2 = '';
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].forEach(function(e){
  szorzotabla2 += e + ' * ' + 4 + ' = ' + e * 4 + '\n';
})

var szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var szorzotabla3 = '';
var sorok = szamok.map(function(e){
  return e + ' * ' + 4 + ' = ' + e * 4;
})
szorzotabla3 = sorok.join('\n');

console.log(szorzotabla3);
