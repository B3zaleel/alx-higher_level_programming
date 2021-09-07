#!/usr/bin/python3
def print_last_digit(number):
    '''
    Prints the last digit of a number and returns its value

    Parameters:
    number (int): The number
    '''
    print('{:s}'.format(str(number)[-1]), end='')
    return int(str(number)[-1])
