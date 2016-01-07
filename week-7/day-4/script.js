'use strict';

console.log('mukodik');

var cim = document.querySelector('.majom');

console.log(cim);

cim.classList.add('piros');

var majomkep = document.querySelector('img');

majomkep.setAttribute('src', 'https://41.media.tumblr.com/84729c469ca431c8c80dad1cd4281205/tumblr_o08zo7SJan1tx21ogo1_540.jpg')


var masikKep = document.createElement('img');

masikKep.setAttribute('src', "http://33.media.tumblr.com/560c6bd597ab217cec337b24e66ddf5e/tumblr_nr3rqa7R5R1rqbio6o1_400.gif");

var bodyvaltozoban = document.querySelector('body')
bodyvaltozoban.appendChild(masikKep);

var bodyvar = document.querySelector('body');

function kepcsinalo(src) {
   var ujkep = document.createElement('img');
   ujkep.setAttribute('src', src)
   bodyvar.appendChild(ujkep);
}
var kepek = [
   'http://lorempixel.com/400/200/sports/',
   'http://lorempixel.com/400/200/sports/',
   'http://lorempixel.com/400/200/sports/',
   'http://lorempixel.com/400/200/sports/',
   'http://lorempixel.com/400/200/sports/',
   'http://lorempixel.com/400/200/sports/',
   'http://lorempixel.com/400/200/sports/',
   'http://lorempixel.com/400/200/sports/',
   'http://lorempixel.com/400/200/sports/',
   'http://lorempixel.com/400/200/sports/',
   'http://lorempixel.com/400/200/sports/'
];

for (var i = 0; i < kepek.length; i++) {
   kepcsinalo(kepek[i]+i+'/');
}


//----------------------------------------------------

var gomb = document.querySelector('.csinal');

gomb.addEventListener('click',
function () {
   alert('kattintottam');
})





