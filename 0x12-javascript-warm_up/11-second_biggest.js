#!/usr/bin/node
/**
 * searches the second biggest integer in a list of args
 */
const args = process.argv.slice(2).map(Number);
const numArgs = args.length;

if (numArgs <= 1){
    console.log(0);
}
else
{
    args.sort((a, b) => b - a);
    console.log(args[1]);
}
