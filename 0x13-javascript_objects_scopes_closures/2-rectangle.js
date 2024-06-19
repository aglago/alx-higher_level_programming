#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    const condition = w <= 0 || h <= 0 || !w || !h;
    if (!condition) {
      this.width = w;
      this.height = h;
    }
  }
};
