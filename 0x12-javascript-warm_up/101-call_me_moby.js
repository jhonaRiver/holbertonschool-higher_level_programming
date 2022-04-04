#!/usr/bin/node
// function that executes x times a function
function callMeMoby (x, theFunction) {
  let num = 0;
  while (num < x) {
    theFunction();
    num++;
  }
}
exports.callMeMoby = callMeMoby;
