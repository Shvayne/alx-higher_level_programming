#!/usr/bin/node
/**
 * A function that returns a list, reversed
 */
exports.esrever = function (list) {
    let newList = [];
    for (let i = list.length - 1; i >= 0; i--){
        newList.push(list[i]);
    }
    return newList;
}