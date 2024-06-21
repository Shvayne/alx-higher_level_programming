#!/usr/bin/node
/**
 * A scipt that imports an array and
 * coomputes a new array
 */
const list = require('./100-data.js');
const newList = list.map((num, index) => value * index);
console.log(list);
console.log(newList);
