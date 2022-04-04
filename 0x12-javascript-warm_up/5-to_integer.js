#!/usr/bin/node
// script that prints My number: <first argument converted in integer>
const argNum = process.argv[2];
if (isNaN(argNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argNum);
}
