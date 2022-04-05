#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js
class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let size = 0;
    if (c === undefined) {
      c = 'X';
    }
    while (size < this.height) {
      console.log(c.repeat(this.width));
      size++;
    }
  }
}
module.exports = Square;
