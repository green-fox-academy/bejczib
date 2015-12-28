function accum(s) {
  var result = '';
  for(var i=0; i<s.length-1; i++) {
    result += s.charAt(i).toUpperCase();
    var j=0;
    while(j<i) {
      result += s.charAt(i).toLowerCase();
      j++;
      }
    result += '-';
  }
  result += s.charAt(s.length-1).toUpperCase();
  var z =0;
  while (z<s.length-1){
    result += s.charAt(s.length-1).toLowerCase();
    z++;
  }
 return result;
}

accum('ZpglnRxqenU');
