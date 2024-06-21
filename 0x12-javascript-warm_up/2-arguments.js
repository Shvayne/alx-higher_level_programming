#!/usr/bin/node
/**
 * Prints a message depending on the number
 * of arguments passed
 */
if (process.argv.length === 2){
    console.log('No Argument');
} else if (process.argv.length === 3){
    console.log('Argument found');
} else if (process.argv.length > 3){
    console.log('Arguments found');
}

