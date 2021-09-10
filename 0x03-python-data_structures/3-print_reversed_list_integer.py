#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''
    Prints the items of a list in a reversed order

    Parameters:
    my_list (list): The list of integers
    '''
    for num in reversed(my_list):
        print('{:d}'.format(num))
