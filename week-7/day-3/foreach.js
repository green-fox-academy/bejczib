'use strict'


var alma = [1,2,3,4,5,6,7,8,9,10];

alma.forEach(function  (e) {console.log(e + '*' + 4 + '=' + e * 4)})

// the same exercise with map


console.log(alma.map((e) => e + '*' + 4 + '=' + e * 4).join('\n'));
