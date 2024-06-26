#!/usr/bin/node
/**
 * Prints "My number: <first argument converted to integer>"
 * if the first argument can be converted to an integer.
 */
const num = Number(process.argv[2]);
if (isNaN(num)){
    console.log('Not a number');
} else {
    console.log(`My number: ${num}`);
}
