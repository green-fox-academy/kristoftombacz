'use strict';

var humwee = {
  type: 'Rendes Katonai Hummer',
  color: 'Terep',
  km: 2e4,
  ride: function ride(km) {
  this.km += km;
  }
};

humwee.ride(554)

console.log(humwee.km)
