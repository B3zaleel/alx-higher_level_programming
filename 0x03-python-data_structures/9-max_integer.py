#!/usr/bin/python3
def max_integer(my_list=[]):
    '''
    Finds the biggest integer in a list of integers

    Parameters:
    my_list (list): The list of integers

    Return:
    None if my_list is empty, otherwise the maximum integer in the list
    '''
    max_num = 0
    for num in my_list:
        max_num = num if num >= max_num else max_num
    return None if len(my_list) == 0 else max_num
