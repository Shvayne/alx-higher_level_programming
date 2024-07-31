#!/usr/bin/node
/* This script writes to a file */

const fs = require('fs');
const fileName = process.argv[2];
const text = process.argv[3];

fs.writeFile(fileName, text, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
