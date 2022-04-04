#!/usr/bin/node
// function that increments and calls a function
function addMeMaybe (num, thefunc) {
  thefunc(num + 1);
}
exports.addMeMaybe = addMeMaybe;
