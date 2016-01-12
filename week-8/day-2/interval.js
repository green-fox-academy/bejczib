'use strict';



var interval = setInterval(function () {
    console.log('puc');
}, 500);

setTimeout(function() {
    console.log('boom');
    clearInterval(interval);
}, 5000);
