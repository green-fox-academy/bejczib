'use strict';

var bodyvar = document.querySelector('body');
var pic = document.querySelector('.kep');
var first_pic = document.querySelector('.first_pic');

function changePicture(src) {
   pic.setAttribute('src', src)
}

function clickPicture(src) {
   pic.setAttribute('src', src)
}

function nextPicture() {
   if (picturePosition === pictures.length-1) {
      next.style.visibility = "hidden"
   } else {
      changePicture(pictures[++picturePosition]);
      prev.style.visibility = "visible";
   }
   console.log(picturePosition);
      actives = container.querySelectorAll('.active')
      for (var i=0;i<actives.length;i++) {
         actives[i].classList.remove('active');
      }
      document.getElementById('pic' + picturePosition).classList.add('active')
}

function prevPicture() {
   if(picturePosition === 0) {
      prev.style.visibility = "hidden"
   } else {
      changePicture(pictures[--picturePosition]);
      next.style.visibility = "visible";
   }
      actives = container.querySelectorAll('.active')
      for (var i=0;i<actives.length;i++) {
         actives[i].classList.remove('active');
      }
      document.getElementById('pic' + picturePosition).classList.add('active');
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

var picturePosition = 0;
var next = document.querySelector('.next');
var prev = document.querySelector('.previous');
first_pic.classList.add('active');
var container = document.querySelector('.container');
var actives = container.querySelectorAll('.active');

next.addEventListener('click',
   function () {nextPicture();});

prev.addEventListener('click',
   function () {prevPicture();});


container.addEventListener('click',
   function (event) {
      var picture_src = event.target.getAttribute('src')
      clickPicture(picture_src);
      picturePosition = pictures.indexOf(picture_src);
      actives = container.querySelectorAll('.active')
      for (var i=0;i<actives.length;i++) {
         actives[i].classList.remove('active');
      }
      event.target.classList.add('active');
   })

document.addEventListener("keypress", keyEventHandler);
function keyEventHandler(e) {
    var keyCode = e.keyCode;
    console.log(e.keyCode);
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

