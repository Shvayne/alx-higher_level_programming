#!/usr/bin/node
/**
 * A function that returns the number of occurences
 * in a list
 */
exports.nbOccurences = function (list, searchElement) {
    return list.filter(element => element === searchElement).length;
}