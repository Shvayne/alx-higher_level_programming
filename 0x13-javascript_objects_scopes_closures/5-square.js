#!/usr/bin/node

const Rectangle = require("./4-rectangle");

/**
 * A square class that inherits from the rectangle class
 */
class Square extends Rectangle{
    constructor(size){
        super(size, size);
    }
}
module.exports = Square;
