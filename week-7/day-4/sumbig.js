'use strict';

function sumStrings(a,b) {
    var bigger = getBigger(a,b).length != 0 ? getBigger(a,b).split('') : ['0'];
    var smaller = getSmaller(a,b).length != 0 ? getSmaller(a,b).split('') : ['0'];
    var biggerIndex = bigger.length-smaller.length;
    var temp = '';
    var result = '';
    for (var i=smaller.length-1;i>=0;i--) {
        var sum = Number(temp);
        sum += Number(smaller[i]) + Number(bigger[i+biggerIndex]);
        temp = '';
        smaller.splice(i, 1);
        bigger.splice(i+biggerIndex, 1);
        if (sum === 0 && i === 0) {sum = ''};
        if (String(sum).length == 2 && sum != 0) {
            temp = String(sum).charAt(0);
            sum = String(sum).charAt(1);
        }
        result+= sum;
    }
    if (bigger.length != 0) {
        for(var j=bigger.length-1;j>=0;j--) {
            console.log(temp);
            if (temp != '' ) {
                var sum2= Number(bigger[j])+ Number(temp);
                temp = '';
                bigger.splice(j, 1);
                var temp2 = '';
                if (String(sum2).length == 2 ) {
                    temp2 = String(sum2).charAt(0);
                    sum2 = String(sum2).charAt(1);
                }
            } else  {
                sum2 = bigger[j];
                console.log(sum2);
            }
            result += sum2
            if ( temp2 != '') {
                console.log('cssss')
                result += temp2;
            }
        }
    } else if (bigger.length === 0 && temp != '') {
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

console.log('131151201344081895336534324866')
console.log(sumStrings('50095301248058391139327916261','81055900096023504197206408605'));




