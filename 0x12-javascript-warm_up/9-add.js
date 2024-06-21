#!/usr/bin/node
/**
 * print the addition of two integers
 */
function add(a, b){
    let num1 = Number(process.argv[2]);
    let num2 = Number(process.argv[3]);
    if (isNaN(num1) || isNaN(num2)){
        console.log('NaN');
    } else {
        console.log(`${num1} + ${num2}`);
    }
}

