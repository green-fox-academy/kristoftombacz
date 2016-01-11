function szorzo(num) {
  for (var i = 1; i < num + 1; i++) {
    for (var j = 1; j < num + 1; j++) {
      console.log(i + " * " + j + " = " + i * j);
    }
    console.log('');
  }
}

function szorzotabla() {
  szorzo(10);
}

szorzotabla();
