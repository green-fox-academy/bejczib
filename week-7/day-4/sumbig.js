'use strict';

function sumStrings(a,b) {
    var bigger = getBigger(a,b).length != 0 ? getBigger(a,b).split('') : ['0'];
    var smaller = getSmaller(a,b).length != 0 ? getSmaller(a,b).split('') : ['0'];
    var biggerIndex = bigger.length-smaller.length;
    var temp = '';
    var result = '';
    for (var i=smaller.length-1;i>=0;i--) {
        var sum = Number(temp);
        temp = '';
        sum += Number(smaller[i]) + Number(bigger[i+biggerIndex]);
        if (sum === 0 && i === 0) {sum = ''};
        smaller.splice(i,1);
        bigger.splice(i+biggerIndex, 1);
        if (String(sum).length == 2 ) {
            temp = String(sum).charAt(0);
            sum = String(sum).charAt(1);
        }
        result+= sum;
    }
    if (bigger.length != 0) {
        for(var j=bigger.length-1;j>=0;j--) {
            if (temp != '' ) {
                sum= Number(bigger[j])+ Number(temp);
                temp = '';
                bigger.splice(j, 1);
                if (String(sum).length == 2 ) {
                    temp = String(sum).charAt(0);
                    sum = String(sum).charAt(1);
                }
            } else if (bigger[j] != '0') {
                sum = bigger[j];
            }
            result += sum
        }
    }
    if (bigger.length === 0 && temp != '') {
        result += temp;
    }
    return result.split('').reverse().join('');
}

function getBigger(a,b) {
    return a.length > b.length ? a : b;
}

function getSmaller(a,b) {
     return a.length > b.length ? b : a;
}

console.log(sumStrings('999','1'));




