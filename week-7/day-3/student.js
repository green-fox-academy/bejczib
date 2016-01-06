'use strict';

function Student(grades) {
    this.grades = grades;
    this.addGrade = function(grade) {
        this.grades.push(grade);
    }
    this.getAverage = function() {
        return this.grades.reduce((a,b) => a+b) / this.grades.length;
    }
}

var karcsi = new Student([]);

karcsi.addGrade(5);
karcsi.addGrade(4);
karcsi.addGrade(1);
karcsi.addGrade(2);
karcsi.addGrade(3);
console.log(karcsi.grades)
console.log(karcsi.getAverage())
