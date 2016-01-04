var arr = [1,2,3,4,5];

function summer() {
    var result = 0;
    arr.map(function(x) {return result += x})
    return result;
}

console.log(summer(arr));
