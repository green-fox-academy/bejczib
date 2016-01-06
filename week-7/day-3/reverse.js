'use strict';

function reverse(string) {
    var result = '';
    for (var i=string.length-1;i>=0;i--) {
        result += string[i];
    }
    return result
}


console.log(reverse('alma'));



function reverseRec(string, num) {
    if (num < 0) {
        return ''
    } else {
        return string[num] + reverseRec(string, num-1)
    }
}

console.log(reverseRec('kacsa', 4));

