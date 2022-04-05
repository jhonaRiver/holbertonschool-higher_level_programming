#!/usr/bin/node
// script that imports an array and computes a new array
const list = require('./100-data.js').list;
console.log(list);
let idx = 0;
const newList = list.map(x => x * idx++);
console.log(newList);
