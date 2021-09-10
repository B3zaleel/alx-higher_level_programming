#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''
    Adds the first two items of the 2 given tuples

    Parameters:
    tuple_a (tuple): The first tuple
    tuple_b (tuple): The first tuple

    Return:
    A tuple consisting of the sum of the first two items in the given tuples
    '''
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    res = (a0 + b0, a1 + b1)
    return res
