'use strict';

function Student() {

  this.grades = [];
  this.addGrade = addGrade;
  this.getAverage = getAverage;
};

function addGrade(num) {
    this.grades.push(num);
};

function getAverage() {
  var sum = 0;
  this.grades.forEach(function (e) {
    sum += e;
  });
  return sum / this.grades.length;
};

// not working
function getAverageReduce() {
  this.grades.reduce(function(acc, num) {
    return acc + num;
  }, 0);
};

var jozsi = new Student();

jozsi.addGrade(4);
jozsi.addGrade(3);
jozsi.addGrade(5);
jozsi.addGrade(5);
console.log(jozsi.getAverage());
