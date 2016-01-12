'use strict';


var fs = require('fs');

fs.readFile('alma.txt', function(error, content) {
    console.log(String(content));
});

console.log('END');
