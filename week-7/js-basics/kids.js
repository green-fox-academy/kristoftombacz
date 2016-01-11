'use strict';

var kids = [
  {name: 'Tibor', candies: 2},
  {name: 'Jozsi', candies: 4},
  {name: 'Steve', candies: 0},
  {name: 'Zakarias', candies: 7},
  {name: 'Julika', candies: 3}
];

function getRichestKidName(kids) {
  var richestKid = kids[0];

  for (var i = 0; i < kids.length; i++) {
    if (richestKid.candies < kids[i].candies) {
      richestKid = kids[i];
    }
  }
  return richestKid.name;
}
