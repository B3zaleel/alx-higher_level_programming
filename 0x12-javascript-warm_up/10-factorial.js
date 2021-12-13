#!/usr/bin/node
/**
 * factorial - Computes the factorial of a number.
 * @param {Number} num - The number.
 *
 * @returns The factorial of the number.
 */
const factorial = (num = NaN) => {
  if (Number.isNaN(num) || (num === 1)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
};

console.log(factorial(Number.parseInt(process.argv[2])));
