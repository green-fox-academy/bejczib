'use strict';


function pascalTriangle(number) {
    var space = '';
    var triangle = [[1]];
    var num;

  for (var j = 0; j < number-1; j++) {
    num = [1];
    for (var k = 1; k < triangle[j].length; k++) {
      num[k] = triangle[j][k] + triangle[j][k-1];
    }
    num.push(1);
    triangle.push(num);
  }
  for (var i=0;i<number;i++) {
        space = '.'.repeat(number-i);
        console.log(space + triangle[i]);
    }

}


pascalTriangle(7)
