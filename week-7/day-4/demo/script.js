'use strict';

var pictures = [
   'http://lorempixel.com/600/400/nature/1/',
   'http://lorempixel.com/600/400/nature/2/',
   'http://lorempixel.com/600/400/nature/3/',
   'http://lorempixel.com/600/400/nature/5/',
   'http://lorempixel.com/600/400/nature/6/',
   'http://lorempixel.com/600/400/nature/7/',
   'http://lorempixel.com/600/400/nature/8/',
   'http://lorempixel.com/600/400/nature/4/',
   'http://lorempixel.com/600/400/nature/10/'
];

function createThumbnail() {
   for (var i=0;i<pictures.length;i++) {
      var thumbnail_pic = document.createElement('img');
      thumbnail_pic.src = pictures[i];
      thumbnail_pic.setAttribute('class', i === 0 ? 'first_pic' : 'small_pic');
      thumbnail_pic.setAttribute('id', 'pic' + i);
      thumbnail.appendChild(thumbnail_pic);
   }
}

var bodyvar = document.querySelector('body');
var pic = document.querySelector('.kep');
var thumbnail = document.querySelector('.thumbnail');
createThumbnail();
var first_pic = document.querySelector('.first_pic');
first_pic.classList.add('active');
var actives = thumbnail.querySelectorAll('.active');
var picturePosition = 0;
var next = document.querySelector('.next');
var prev = document.querySelector('.previous');

function markActive() {
   actives = thumbnail.querySelectorAll('.active')
   for (var i=0;i<actives.length;i++) {
      actives[i].classList.remove('active');
   }
   document.getElementById('pic' + picturePosition).classList.add('active')
}

function changePicture(src) {
   pic.setAttribute('src', src)
}

function clickPicture(src) {
   pic.setAttribute('src', src)
}


function nextPicture() {
   if (picturePosition === pictures.length-1) {
      next.style.visibility = "hidden";
   } else {
      changePicture(pictures[++picturePosition]);
      prev.style.visibility = "visible";
   }
   markActive();
}

function prevPicture() {
   if (picturePosition === 0) {
      prev.style.visibility = "hidden"
   } else {
      changePicture(pictures[--picturePosition]);
      next.style.visibility = "visible";
   }
   markActive();
}

next.addEventListener('click',
   function () {nextPicture();});

prev.addEventListener('click',
   function () {prevPicture();});

thumbnail.addEventListener('click',
   function (event) {
      var picture_src = event.target.getAttribute('src')
      clickPicture(picture_src);
      picturePosition = pictures.indexOf(picture_src);
      markActive();
   })

document.addEventListener("keypress", keyEventHandler, false);
function keyEventHandler(e) {
    var keyCode = e.keyCode;
    console.log(keyCode)
    if(keyCode === 97) {
      if ( picturePosition === 0) {
         picturePosition = pictures.length;
      }
        prevPicture();
    } else if (keyCode == 100) {
      if ( picturePosition === pictures.length-1) {
         picturePosition = -1;
      }
      nextPicture();
    }
};

