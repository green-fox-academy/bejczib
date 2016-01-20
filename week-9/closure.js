'use strict';

// function createCounter(start) {

//     return function() {
//         start++;
//         return start;
//     }
// }

// var counter = createCounter(5)
// console.log(counter())
// console.log(counter())

// var counter2 = createCounter(5)
// console.log(counter2())
// console.log(counter2())




'use strict';
function createCar(color, type, km) {
  function ride(distnace) {
    km += distance;
  }
  function getKm(argument) {
    return km;
  }
  return {
    ride:ride,
    getKm:getKm
  };
}
var opel = createCar('white', 'opel', 4000);
opel.ride(100);
