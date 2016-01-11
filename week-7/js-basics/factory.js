'use strict';

function createCar(color, type, km) {
  return {
    color: color,
    type: type,
    km: km,
    ride: function(km) {
      this.km += km
    }
  }
}

var volvo = createCar('sarga', 's50', 0);

volvo.ride(123);
console.log(volvo.km);
