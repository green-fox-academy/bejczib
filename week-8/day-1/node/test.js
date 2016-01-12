'use strict';

var arabic2Roman = require('./kata.js')
var tape =require('tape');

tape('roman converter', function (t) {
    t.equal(arabic2Roman(0),'');

    t.end();
});

