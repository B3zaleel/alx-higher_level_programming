#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''
    Finds all multiples of 2 in a list

    Parameters:
    my_list (list): The list of integers

    Return:
    A list of bools specifying the divisibility of the number with 2
    at the same position in the given list
    '''
    res = []
    for num in my_list:
        res.append(num % 2 == 0)
    return res
