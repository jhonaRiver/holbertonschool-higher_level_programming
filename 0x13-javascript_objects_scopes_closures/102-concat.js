#!/usr/bin/node
// script that concats 2 files
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');
const txtA = fs.readFileSync(fileA);
const txtB = fs.readFileSync(fileB);
fs.writeFileSync(fileC, txtA + txtB);
