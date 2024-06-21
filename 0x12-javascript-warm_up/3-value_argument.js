#!/usr/bin/node
/**
 * prints the value of the first arg passed to it
 */
if (process.argv[2] === undefined){
    console.log('No argument');
}else{
    console.log(process.argv[2]);
}
