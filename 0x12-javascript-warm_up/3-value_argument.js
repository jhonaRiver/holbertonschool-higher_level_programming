#!/usr/bin/node
// script that prints the first argument passed to it

// first argument
const first = process.argv[2];

if (first === undefined) {
  console.log('No argument');
} else {
  console.log(first);
}
