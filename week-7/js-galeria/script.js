'use strict';

var imgBox = document.querySelector('.img');
var arrowLeft = document.querySelector('.arrow-left');
var arrowRight = document.querySelector('.arrow-right');
var thumb = document.querySelector('.thumb-img');
var actualPos = 0;

var imgArray = [
  'img/1.jpg',
  'img/2.jpg',
  'img/3.png',
  'img/4.jpg',
  'img/5.gif',
]

thumb.addEventListener('click', function(){
  imgBox.setAttribute('src', thumb.getAttribute('src'));
});

arrowLeft.addEventListener('click', function(){
  imgBox.setAttribute('src', getImg('left'));
});

arrowRight.addEventListener('click', function(){
  imgBox.setAttribute('src', getImg('right'));
});

arrowLeft.addEventListener('mouseover', mouseOver('left'), false);
arrowLeft.addEventListener('mouseenter', mouseEnter('left'), false);
arrowRight.addEventListener('mouseover', mouseOver('right'), false);
arrowRight.addEventListener('mouseenter', mouseEnter('right'), false);

function mouseEnter (direction) {
  if (direction === 'left') {
    arrowLeft.setAttribute('src', 'img/arrow-left2.png');
  } else if (direction === 'right') {
    arrowRight.setAttribute('src', 'img/arrow-right2.png');
  }
}

function mouseOver (direction) {
  if (direction === 'left') {
    arrowLeft.setAttribute('src', 'img/arrow-left.png');
  } else if (direction === 'right') {
    arrowRight.setAttribute('src', 'img/arrow-right.png');
  }
}

function setNewImg (direction) {
  if (direction === 'left') {
    actualPos -= 1;
    return imgArray[actualPos];
  } else if (direction === 'right') {
    actualPos += 1;
    return imgArray[actualPos];
  }
}

function getImg(direction) {
  if (imgBox.getAttribute('src') === imgArray[0] && direction === 'left'){
    return imgArray[0];
  }else if (imgBox.getAttribute('src')===imgArray[4] && direction=== 'right') {
    return imgArray[4];
  }
  else {
//    setNewImg(direction);
  if (direction === 'left') {
    actualPos -= 1;
    return imgArray[actualPos];
  } else if (direction === 'right') {
    actualPos += 1;
    return imgArray[actualPos];
  }
  }
}
