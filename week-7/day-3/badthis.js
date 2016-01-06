// 'use strict';

var student  = {
    age: 10,
    sayYourAge: sayYourAge
};

function sayYourAge() {
    console.log("i am " + this.age);
}

student.sayYourAge();

sayYourAge();
