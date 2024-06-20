#!/usr/bin/node
/**
 * prints C is first X times
 */
let num = Number(process.argv[2]);
if (isNaN(num)){
    console.log("Missing number of occurrences")
} else {
    for(let i = 0; i < num; i++){
        console.log("C is fun");
    }
}