#!/usr/bin/node
/*
 * this file reads and prints the contents of a file provided as arg
 */
const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
