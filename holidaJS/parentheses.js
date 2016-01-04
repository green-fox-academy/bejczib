function validParentheses(parens){
  var par= parens.split('');
  result = 0;
  console.log(par)
  for(var i=0;i<par.length;i++) {
    a = par[i];
    console.log(a);
    for(var j=1;j<par.length;j++) {
      b = par[j];
      console.log(b);

      if(a+b == '()') {
        result += 1;
      }
    }
  }
return result;
}


console.log(validParentheses('()('))
