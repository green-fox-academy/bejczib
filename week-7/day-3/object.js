'use strict';

var humwee = {
    type: 'Rendes katonai',
    color: 'terep',
    km: 20000,
    ride: function ride(km) {
        this.km += km;
    }
};


humwee.ride(200);

console.log(humwee.km);

