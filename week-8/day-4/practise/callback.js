'use strict';


// function runIn5Seconds(cb) {
//     setTimeout(cb, 5000);
// }

// runIn5Seconds(function () {
//     console.log('jaa');
// })



var fs = require('fs');

fs.readFile('alma.txt', function(err, content) {
    console.log(String(content));
})


// function letterInAlmaTxt(letter, cb) {
//     fs.readFile('alma.txt', function(err, content) {
//         var count = 0;
//         for (var =0; i<String(content).length;i++) {
//             if (letter === String(content)[i]) {
//                 count++;
//             }
//         }
//         cb(count);
// })
// }


function getFirstIndexInAlmaTxt(letter, cb) {
    var fs = require('fs');
    fs.readFile('alma.txt', function(err, content) {

})
}
