#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let charact;

    if (c) {
      charact = c;
    } else {
      charact = 'X';
    }

    let square = '';

    for (let i = 0; i < this.size; i++) {
      for (let k = 0; k < this.size; k++) {
        square = square + charact;
      }

      if (i < this.size - 1) {
        square = square + '\n';
      }
    }
    console.log(square);
  }
};
