'use strict';

function Student() {
  this.grades = {};
  this.addGrade = addGrade;
  this.getAverage = getAverage;
  this.getCount = getCount;
};

function getCount() {
  var output = {};
  for (var subject in this.grades) {
    output[subject] = this.grades[subject].length;
  }
  return output;
};

function addGrade(subject, grade) {
  if (this.grades[subject] === undefined) {
    this.grades[subject] = [];
  }
  this.grades[subject].push(grade);
};

function getAverage() {
  var sum = 0;
  var count = 0;
  for (var subject in this.grades){
    this.grades[subject].forEach(function (grade){
      sum += grade;
      count++;
    })
  }
  return sum / count;
};
var dezso = new Student();

dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 5);
dezso.addGrade('rajz', 5);
dezso.addGrade('magyar', 5);
console.log(dezso.getCount()); // 'rajz': 2, 'matek': 3
console.log(dezso.getAverage()); // 3.4

//szorgalmi

//deszo.getAverageBySubject();
