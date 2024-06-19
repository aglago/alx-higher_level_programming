#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    const condition = w <= 0 || h <= 0 || !w || !h;
    if (!condition) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';

    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        rect = rect + 'X';
      }

      if (i < this.height - 1) {
        rect = rect + '\n';
      }
    }
    console.log(rect);
  }
};
