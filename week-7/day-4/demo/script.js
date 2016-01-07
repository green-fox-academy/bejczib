'use strict';

var bodyvar = document.querySelector('body');
var pic = document.querySelector('.kep');

function changePicture(src) {
   pic.setAttribute('src', src)
}

var pictures = [
   'http://lorempixel.com/600/400/sports/1/',
   'http://lorempixel.com/600/400/sports/2/',
   'http://lorempixel.com/600/400/sports/3/',
   'http://lorempixel.com/600/400/sports/5/',
   'http://lorempixel.com/600/400/sports/6/',
   'http://lorempixel.com/600/400/sports/7/',
   'http://lorempixel.com/600/400/sports/8/',
   'http://lorempixel.com/600/400/sports/9/',
   'http://lorempixel.com/600/400/sports/10/'
];

var picture = 0;
var next = document.querySelector('.next');
var previous = document.querySelector('.previous');

next.addEventListener('click',
   function () {
      picture === pictures.length-1 ? picture = 0 : changePicture(pictures[++picture]);
});

previous.addEventListener('click',
   function () {
      picture === 0 ? picture = pictures.length-1 : changePicture(pictures[--picture]);
});
