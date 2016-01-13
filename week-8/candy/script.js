'use strict';

function Candy() {
  this.candycount = 120;
  this.lollipopcount = 0;
  this.velocitycount = 0;

  this.candies = document.querySelector('.candies');
  this.lollipops = document.querySelector('.lollipops');
  this.velocity = document.querySelector('.velocity');
  this.buyCandy = document.querySelector('.buyCandy');
  this.creatLollipop = document.querySelector('.creatLollipop');
  this.creatLollipop100 = document.querySelector('.creatLollipop100');

  this.addCandy = addCandy;
  this.getVelocity = getVelocity;
  this.refresh = refresh;
  this.ifLollipop10 = ifLollipop10;
  this.gameWon = gameWon;
  this.disableButton = disableButton;
  this.buyLollipopFor = buyLollipopFor;

  var _this = this;
  this.refresh();

  function addCandy(number){
    _this.candycount += number;
    _this.refresh();
  }
  function getVelocity(){
    return Math.floor(_this.lollipopcount / 10);
  }
  function refresh(){
    _this.candies.innerText = _this.candycount;
    _this.lollipops.innerText = _this.lollipopcount;
    _this.velocity.innerText = _this.velocitycount;
  }
  function ifLollipop10(){
    if (_this.lollipopcount >= 10){
      _this.addCandy(_this.getVelocity());
    }
  }
  function gameWon(number) {
    if (_this.candycount > number-1){
      alert('You WON!');
      document.location.reload();
    }
  }
  function disableButton(number, button){
    if (_this.candycount >= number-1){
      button.disabled = false;
    } else {
      button.disabled = true;
    }
  }
  function buyLollipopFor(number){
    if (_this.candycount >= number){
      _this.candycount -= number;
      _this.lollipopcount += number / 10;
      _this.velocitycount = _this.getVelocity();
      _this.refresh();
    }
  }

  this.buyCandy.addEventListener('click', function() {
    _this.addCandy(1);
  })
  this.creatLollipop.addEventListener('click', function() {
    _this.buyLollipopFor(10);
  })
  this.creatLollipop100.addEventListener('click', function() {
    _this.buyLollipopFor(100);
  })

  setInterval (function() {
    _this.disableButton(10, _this.creatLollipop);
    _this.disableButton(100, _this.creatLollipop100);
    _this.ifLollipop10();
    _this.gameWon(1500);
  }, 1000);
}

var jatek = new Candy();
