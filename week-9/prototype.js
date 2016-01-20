'use strict';

// function Car(color, type, km) {
//     this.color = color;
//     this.type = type;
//     this.km = km;

//     this.ride = function(km) {
//         this.ride += km;
//     }
// }

// var uaz = new Car('lila', 'UAZ', 300000);

// uaz.ride(60);





function Car2(color, type, km) {
    this.color = color;
    this.type = type;
    this.km = km;
}

Car2.prototype.ride = function (km) {
    this.km += km;
}
