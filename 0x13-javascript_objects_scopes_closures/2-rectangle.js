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
}
module.exports = Rectangle;
