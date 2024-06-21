#!/usr/bin/node
/**
 * A function that prints the number of args printed and new vale
 */
exports.logMe = (function (){
    let count = 0;
    return function (item) {
        console.log(`${count}: ${item}`);
        count++;
    };
})();