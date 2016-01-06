'use strict';

var kids = [
{name: 'Tibor', candles: 2},
{name: 'Jozsi', candles: 3},
{name: 'Agoston', candles: 0},
{name: 'Julika', candles: 10},
{name: 'Zakarias', candles: 4},
];


// function getTheRichestKidsName(kids) {
//     var max = kids[0].candles;
//     var name_kid = kids[0].candles;
//     for (var i=0;i<kids.length;i++) {
//         if (kids[i].candles > max) {
//             max = kids[i].candles;
//             name_kid = kids[i].name;
//         }
//     }
//     return name_kid;
// }
// console.log(getTheRichestKidsName(kids))


console.log(kids.reduce(function(a,b) {return a.candles > b.candles ? a : b}).name)







console.log([1,2,3,57,5,3].reduce(function(a,b) {return Math.max(a,b)}))
