function alma(string) {
    var stringWords = string.split(' ');
    if( stringWords.length == 1) {
    var stringChar = string.split('')
    for(var i=0;i<stringChar.length;i++) {
        if (i % 2 == 0) {
            stringChar.splice(i,1,stringChar[i].toUpperCase())
        }
     }
     return stringChar.join('');
 }
 else {
    var result = '';
    for(var j=0;j<stringWords.length;j++) {
        var stringWordsChar = stringWords[j].split('');
        for(var k=0;k<stringWordsChar.length;k++) {
             if (k % 2 == 0) {
            stringWordsChar.splice(k,1,stringWordsChar[k].toUpperCase());
        }
        result += stringWordsChar[k];
        }
        if (j!=stringWords.length-1) {
        result += ' ';
    }
    }
    return result;
 }

}
console.log(alma('alma korte'));
