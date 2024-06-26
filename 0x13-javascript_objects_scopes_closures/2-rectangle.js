#!/usr/bin/node
/**
 * A rectangle class that defines a rectangle
 * and returns an empty object for any invalid
 * input
 */
class Rectangle {
    constructor(w, h){
        if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger){
            this.width = w;
            this.height = h;
        } else {
            return {};
        }

    }
}
module.exports = Rectangle;
