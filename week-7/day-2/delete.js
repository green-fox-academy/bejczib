String.prototype.delete = function(remove) {
 var result= '';
 for(var i=0;i<this.length;i++) {
    for (var j=0;j<remove.length;j++) {
    if(this.charAt(i) != remove.charAt(j)) {
        result += this.charAt(i)
    }
    }
 }
 return result
}

console.log("Hello World".delete('o'))
