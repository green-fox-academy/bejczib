function isPrim(num) {
    var hasDivisor = 0;
    var i = 2;
    while (i < num) {
        if (num % i ==0) {
            hasDivisor = 1;
        }
        i++
    }

    if(hasDivisor ==1 || num == 0 || num == 1) {
        return false;
    }else {
        return true;
    }
}


function primerow(num) {
    var i=0;
    while (i<num) {
        if (isPrim(i) == true) {
            console.log(i + " is prime");
            i++
        } else if (isPrim(i)== false) {
            console.log(i + " is not prime");
            i++
        }
    }
}

primerow(50)
