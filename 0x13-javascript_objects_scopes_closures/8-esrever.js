#!/usr/bin/node
// function that returns the reversed version of a list
exports.esrever = function (list) {
  const rlist = [];
  let idx = list.length - 1;
  while (idx >= 0) {
    rlist.push(list[idx]);
    idx--;
  }
  return (rlist);
};
