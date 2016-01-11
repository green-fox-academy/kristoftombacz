'use strict';

function Car(color, type, km) {
  this.color = color;
  this.type = type;
  this.km = km;
  this.ride = function(km) {
    this.km += km
  }
}

var golf = new Car('piros', '1es golf', 12344)

golf.ride(99999999999)
console.log(golf.km)
