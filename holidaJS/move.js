function moveZeros(arr) {
    var count = 0;
  while (arr.indexOf(0) != -1) {
    arr.splice(arr.indexOf(0),1);
    count ++;
  }
  for(var i=0;i<=count;i++)
    arr.push(0);
  return arr;
}

console.log(moveZeros([ 9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9 ]))


