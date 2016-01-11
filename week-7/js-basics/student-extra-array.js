'use strict';

function Student() {
  this.grades = [{subject: 'matek', grade: 4}];
  this.addGrade = addGrade;
//  this.getAverage = getAverage;
  this.getCount = getCount;
};

function getCount() {
  var output = {};
  this.grades.forEach(function(grade){
    if (output[grade.subject] === undefined) {
      output[grade.subject] = 0;
    }
    output[grade.subject]++;
  });
  return output;
};

function addGrade(subject, grade) {
  this.grades.push({subject: subject, grade: grade});
};

var dezso = new Student();

dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);
dezso.addGrade('magyar', 3);
dezso.addGrade('foldrajz', 3);
console.log(dezso.getCount()); // 'rajz': 2, 'matek': 3
//dezso.getAverage(); // 3.4

//szorgalmi

//deszo.getAverageBySubject();
