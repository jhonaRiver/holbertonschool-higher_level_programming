#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const args = process.argv.slice(2).map(Number);
let Bigsecond = 0;
if (args.length > 1) {
  Bigsecond = args.sort((a, b) => (b - a))[1];
}
console.log(Bigsecond);
