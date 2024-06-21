#!/usr/bin/node
/**
 * Executes x times a function
 */
function executeXTimes(x, theFunction)
{
    if (x > 0){
        theFunction();
        executeXTimes(x - 1, theFunction);
    }
}
module.exports = executeXTimes;
