'use strict';

var timeout = setTimeout(function() {
    console.log('cuc');
}, 1000);

clearTimeout(timeout);
