#!/usr/bin/node

const Square = require("./5-square");

/**
 * A square class that extends from Square class
 *  and overwrites the print method of the parent class
 */
class Square extends Square {
    charPrint(c){
        if (typeof c === 'undefined') {
            c = 'X';
        }
        if (this.width && this.height) {
            for (let i = 0; i < this.height; i++) {
                console.log(c.repeat(this.width))
            }
        }
    }
}
module.exports = Square;