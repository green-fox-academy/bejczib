var array = [1,2,3,4,5,6,7];
var sum = 0;

function sum_array() {
    for (var i=0; i< array.length; i++) {
        sum +=array[i];
    }
    return sum;
}
console.log(sum_array())
