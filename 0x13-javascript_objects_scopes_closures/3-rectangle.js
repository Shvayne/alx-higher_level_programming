#!/usr/bin/node
/**
 * A rectangle class that defines a rectangle
 * and returns an empty object for any invalid
 * input and prints the rectangle
 */
class Rectangle {
    constructor(w, h){
        if (h > 0 && w > 0 && Number.isInteger(w) && Number.isInteger(h)){
            this.width = w;
            this.height = h;
        } else {
            return {};
        }
    }
    print(){
        if (this.width && this.height){
            const row = 'X'.repeat(this.width);
            for (let i = 0; i < this.height; i++){
                console.log(row);
            }
        }
    }
}
module.exports = Rectangle;
