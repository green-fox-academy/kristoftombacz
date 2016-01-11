'use strict';

console.log('mukodik');

var cim = document.querySelector('h1');
console.log(cim);

cim.classList.add('piros');

var bodyValtozoba = document.querySelector('body');

function kepcsilano(src) {
  var ujKep = document.createElement('img');

  ujKep.setAttribute('src', src);

  bodyValtozoba.appendChild(ujKep);
};

var array = [
  'https://41.media.tumblr.com/19b19ed0dc7af9303de88581c809c61a/tumblr_nb8q4t6zmM1rzcpj8o1_400.png',
  'https://41.media.tumblr.com/8c718ceb79887aa09fa7fc1b03249035/tumblr_nlodr6WofO1tm1x8po1_540.jpg',
  'https://40.media.tumblr.com/66737194594d0a52ed200add1de5cc97/tumblr_inline_o0kzcqq5Fw1rl1jmj_540.png',
  'https://36.media.tumblr.com/1f7383fb850d420844a640be2b314b39/tumblr_nzgkmltpIQ1rmd51zo1_540.jpg',
  'https://40.media.tumblr.com/64fc7503fc27d1afa407c00debe4b72e/tumblr_n8obq2wpnT1rt05ero1_540.jpg',
  'https://45.media.tumblr.com/a587e797cc93c1dda085eb6134207b5d/tumblr_o0ifmzEAYl1ukldkho1_500.gif',
  'https://41.media.tumblr.com/94d04ae689077d6d4ff3cbe3b3ec4cd5/tumblr_o0kxu5urFy1qi6wa0o1_540.jpg',
  'https://36.media.tumblr.com/1765a14c5e523e8ec0bf6b5e07e1668c/tumblr_nxeo7wShCp1rdyfv3o1_540.jpg',
  'https://41.media.tumblr.com/fd4c5b09cb1ed524d0c7c8bf230256ff/tumblr_nyy1tgBrat1qabv7ko1_540.jpg',
  'https://40.media.tumblr.com/4f2789d04c316097631d2ba377fe93f8/tumblr_o0kxceAeBH1qzf4nwo1_540.jpg',
  'https://41.media.tumblr.com/tumblr_lx34xke2RN1r5zq6ao1_500.jpg',
  'https://41.media.tumblr.com/9f92ece1e07120dd664265dd9247be02/tumblr_nu6pmeyjDS1qlzef1o1_540.jpg',
  'https://40.media.tumblr.com/4d6ddbc5064e0625a8709d2faef691e1/tumblr_o0kv9f3LRV1rih7vko1_540.png',
  'https://40.media.tumblr.com/2ab6b8896291bb5f2dceb12264444024/tumblr_mvcdbwpe1I1s4zmm0o1_540.jpg',
  'https://45.media.tumblr.com/10d61378db56b46cd2c56e1ca81ad295/tumblr_o0k40jCN181ub2jsqo1_500.gif',
  'https://36.media.tumblr.com/1f7383fb850d420844a640be2b314b39/tumblr_nzgkmltpIQ1rmd51zo1_540.jpg',
  'https://33.media.tumblr.com/7a9c3636ab14237c651d1a5a9557bf04/tumblr_inline_o0etcwWdHA1raprkq_500.gif',
  'https://49.media.tumblr.com/7835dec06b79a739e8d50fb85711e7a3/tumblr_nskhbiOcPY1tovmb9o1_250.gif',
  'https://45.media.tumblr.com/1c763ee33e32c692c732c2dba4e144f3/tumblr_nskhbiOcPY1tovmb9o2_250.gif',
  'https://49.media.tumblr.com/97951ecef35885e03876382515151f34/tumblr_nskhbiOcPY1tovmb9o3_250.gif',
  'https://45.media.tumblr.com/492aa7772dd15592901e7b5e2a19e2b9/tumblr_nskhbiOcPY1tovmb9o4_250.gif'
]

for (var i = 0; i < array.length; i++) {
  kepcsilano(array[i]);
};

var gomb = document.querySelector('.csinal');

gomb.addEventListener('click', function() {
  kepcsilano('https://41.media.tumblr.com/28b2338d9b83f0fc8ea1bbd5f67ea924/tumblr_o0l4qa8nQi1rgs6q2o1_400.jpg');
})

window.addEventListener('scroll', function () {
  console.log('scroooolll');.59
})

var kutyagomb = document.querySelector('.kutya');
var macskagomb = document.querySelector('.macska');
var valtoskep = document.querySelector('.citakutya');

kutyagomb.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'https://45.media.tumblr.com/23a1ba79a8cfe6269c2eeda9f10d24f0/tumblr_o0kezkShol1s02vreo3_250.gif');
})

macskagomb.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'https://40.media.tumblr.com/ec3b7c78968e08b06af5b7711d3ce6bd/tumblr_o0kj6nrVCH1sg9amyo1_500.jpg');
})
