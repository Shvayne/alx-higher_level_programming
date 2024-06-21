#!/usr/bin/node
/**
 * computes and prints a factorial
 * Factorial of NaN is 1.
 */
function factorial(num)
{
    if (isNaN(num))
    {
        return 1;
    }
    else if (num <= 1)
    {
        return 1;
    }
    else
    {
        return num * factorial(num - 1);
    }
}
const arg = Number(process.argv[2]);
const result = factorial(arg);
console.log(result);
