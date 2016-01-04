names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"];


function whoIsNext(names, r){
var i =1;
while (i <= r) {
    var next = names[0];
    names.splice(0,1);
    names.push(next);
    names.push(next);
    i++;
}
console.log(r);
return next;
}
console.log(whoIsNext(names, 2))
