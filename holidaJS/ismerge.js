function isMerge(s, part1, part2) {
  var s_chars = s.split('');
  var part1_chars = part1.split('');
  var part2_chars = part2.split('');
  var compare = '';
  console.log(s_chars);
  console.log(part1_chars);
  console.log(part2_chars);
  var i = 0;
  while(i<= part1_chars.length) {
      compare += part1_chars[i];
      compare += part2_chars[i];
      i++;
  }
  compare += part2_chars[i:];
  return compare;
}
console.log(isMerge('codewars', 'cdw', 'oears'))
