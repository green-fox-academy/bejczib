'use strict';

function sumStrings(a,b) {

  if (a.length <= String(Number.MAX_SAFE_INTEGER).length/2) {
    return (+a + +b).toString()
  } else {
    var lengthIndex = Math.round(getBigger(a,b).length/2);
    console.log('lengthindex :' + lengthIndex);

    console.log('a :' + a);
    var aHalf1 = a.substr(0,a.length - lengthIndex);
    var aHalf2 = a.substr(a.length -lengthIndex,a.length-1);
    console.log('b :' + b);
    var bHalf1 = b.substr(0,b.length -lengthIndex);
    var bHalf2 = b.substr(b.length - lengthIndex,b.length-1);
    var result2 = (Number(aHalf2) + Number(bHalf2)).toString();
    var temp = result2.toString()[0]
    var result1 = Number(aHalf1) + Number(bHalf1) + Number(temp).toString();
    console.log('aHalf1 :' + aHalf1)
    console.log('bHalf1 :' + bHalf1)
    console.log('aHalf2 :' + aHalf2)
    console.log('bHalf2 :' + bHalf2)
    console.log('result1 :' + result1)
    console.log('result2 :' + result2)
    console.log('131151201344081895336534324866 <--- expected')
    return result1 + result2.substr(1,result2.length-1);

  }
}


function getBigger(a,b) {
    return a.length > b.length ? a : b;
}

console.log(sumStrings('50095301248058391139327916261','81055900096023504197206408605'));



