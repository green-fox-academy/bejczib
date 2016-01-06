'use strict'

function Student() {
    this.grades = {};

    this.addGrade = function(subject, grade) {
        if (this.grades[subject] === undefined) {
            this.grades[subject] = [];
            this.grades[subject].push(grade);
        } else {
            this.grades[subject].push(grade);
        }
    }

    this.getAverage = function() {
        var averages = [];
        for (var subject in this.grades) {
            averages.push(makeAverage(this.grades[subject]));
        }
        return 'The student average: ' + makeAverage(averages).toFixed(2);
    }

    this.gst = function() {
        var db = 0;
        for (var subject in this.grades) {
            console.log(subject + ' : ' + this.grades[subject].length)
            }
    }

    this.getAverageBySubject = function(subject) {
        return 'The average of ' + subject + ' : ' + makeAverage(this.grades[subject]).toFixed(2);
    }

    function makeAverage(subject) {
        return makeSum(subject) / subject.length.toFixed(2);
    }

    function makeSum(subject) {
        return subject.reduce((a,b) => a+b);
    }
}

var dezso = new Student();
dezso.addGrade('matek',3);
dezso.addGrade('matek',4);
dezso.addGrade('matek',4);
dezso.addGrade('tori',5);
dezso.addGrade('tori',3);
dezso.addGrade('tori',4);
dezso.addGrade('tori',1);
dezso.addGrade('rajz',5);
dezso.addGrade('rajz',5);
dezso.addGrade('tesi',4);
dezso.addGrade('tesi',4);
dezso.addGrade('tesi',3);
dezso.addGrade('tesi',5);
dezso.addGrade('tesi',5);

//console.log(dezso.grades);
//console.log(dezso.getAverage());
//console.log(dezso.getAverageBySubject('tori'));
dezso.getCount();



