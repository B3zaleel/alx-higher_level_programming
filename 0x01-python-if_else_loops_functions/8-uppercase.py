#!/usr/bin/python3
def uppercase(str):
    '''
    Prints a string, converting lowercase characters to uppercase

    Parameters:
    str (str): The string to print
    '''
    for i in range(len(str)):
        # is_lower = (ord(str[i]) >= ord('a')) and (ord(str[i]) <= ord('z'))
        end_str = '\n' * (i == (len(str) - 1))
        if str[i].islower():
            print('{:c}'.format(ord(str[i]) - (1 << 5)), end=end_str)
        else:
            print('{:c}'.format(ord(str[i])), end=end_str)
