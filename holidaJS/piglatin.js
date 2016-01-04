function toPig(string){
  if (string.search(/[^a-zA-Z]/)!=-1) return null;
  pos=string.search(/[aeiou]/)
  if (pos==-1) return string+"ay";
  if (pos==0) return string+"way";
  else return string.slice(1,string.length)+"ay";
}

function pigIt(str){
  var words = str.split(' ');
  var mainRes = '';
  for(var i=0;i<words.length;i++) {
    mainRes += toPig(words[i]);
    if(i!=words.length-1) {
      mainRes += ' '
    }
  }
  return mainRes;
}


console.log(pigIt('Pig latin is cool'))
'igPay atinlay siay oolcay'
