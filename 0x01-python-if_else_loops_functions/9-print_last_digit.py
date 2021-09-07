#!/usr/bin/python3
def print_last_digit(number):
    '''
    Prints the last digit of a number and returns its value

    Parameters:
    number (int): The number
    '''
    print(str(number)[-1])
    return int(str(number)[-1])
