'use strict';

function triangle(n) {
    var space = '';
    for (var i=0;i<n;i++) {
        space = '.'.repeat(n-i);
        console.log(space + '#'.repeat(2*i+1));
    }
}

triangle(15);
