function isPrim(num) {
    var hasDivisor = 0;
    var i = 2;
    while (i < num) {
        if (num % i ==0) {
            hasDivisor = 1;
            break
        }
        else {
            i++
        }
    }

    if(hasDivisor ==0 && num != 0 && num != 1) {
        console.log("it's prim!")
    }else {
        console.log("it's not prim!")
    }
}

isPrim(2)
