'use strict'

// var i = 0
// while (i <= 100) {
//     if(i % 3 == 0 && i % 5 == 0) {
//         console.log('fizzbuzz');
//     } else if (i % 5 == 0) {
//         console.log('fizz');
//     } else if (i % 3 == 0) {
//         console.log('buzz');
//     } else {
//         console.log(i);
//     }
//     i++;
// }

for (var j=1; j<=100;j++) {
    if(j % 3 == 0 && j % 5 === 0) {
        console.log('fizzbuzz');
    } else if (j % 5 === 0 || /[5]/.test(j)) {
        console.log('fizz');
    } else if (j % 3 ===n 0 || /[3]/.test(j)) {
        console.log('buzz');
    } else {
        console.log(j);
    }
}
