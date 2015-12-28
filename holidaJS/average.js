function getAverage(marks){
  var sum = 0;
  for(var i=0; i< marks.length; i++) {
        sum += marks[i];
        }
        var result = Math.round(sum / marks.length);
  return result;
}

console.log(getAverage([2,2,2,2]))
