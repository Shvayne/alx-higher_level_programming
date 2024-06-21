#!/usr/bin/node
/**
 * converts a value from base 10 to anybase passed
 */
exports.converter = function (base){
    return function (number) {
        return number.toString(base);
    }
}