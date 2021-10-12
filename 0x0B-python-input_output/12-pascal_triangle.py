#!/usr/bin/python3
'''A module containing combinatorial mathematical functions.
'''


def factorial(n):
    '''Computes the factorial of a number.

    Args:
        n (int): The number whose factorial is to be computed.

    Returns:
        int: The factorial of the given number.
    '''
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


def combination(i, j):
    '''Computes the number of combinations for a given set.

    Args:
        i (int): The total number of items in the set.
        j (int): The number of items to be picked from the set.

    Returns:
        int: The number ways j items can be picked from a set of
        i items in any order.
    '''
    return factorial(i) / (factorial(j) * factorial(i - j))


def pascal_triangle(n):
    '''Generates a list of lists of integers representing the
    Pascal’s triangle of a given integer.

    Args:
        n (int): The st

    Returns:
        list: A list of integers containing the values of their
        respective row in Pascal's triangle for the given number.
    '''
    if type(n) is not int:
        raise Exception('n must be an integer')
    if n <= 0:
        return []
    res = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(int(combination(i, j)))
        res.append(row)
    return res
