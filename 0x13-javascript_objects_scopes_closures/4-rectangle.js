#!/usr/bin/node
// class Rectangle that defines a rectangle
class Rectangle {
  // constructor must take 2 arguments w and h
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // instance method called print() that prints the rectangle using the character X
  print () {
    let x = 0;
    for (x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }

  // instance method called rotate() that exchanges the width and the height of the rectangle
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // instance method called double() that multiples the width and the height of the rectangle by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
