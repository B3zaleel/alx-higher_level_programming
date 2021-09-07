#!/usr/bin/python3
def uppercase(str):
    '''
    Prints a string, converting lowercase characters to uppercase

    Parameters:
    str (str): The string to print
    '''
    for i in range(len(str)):
        c = str[i]
        is_lower = (ord(c) >= ord('a')) and (ord(c) <= ord('z'))
        offset = (1 << 5) if is_lower else 0
        print('{:c}'.format(ord(c) - offset), end='')
    print('')
