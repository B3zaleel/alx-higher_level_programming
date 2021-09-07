#!/usr/bin/python3
def uppercase(str):
    '''
    Prints a string, converting lowercase characters to uppercase

    Parameters:
    str (str): The string to print
    '''
    for i in range(len(str)):
        is_lower = (ord(str[i]) >= ord('a')) and (ord(str[i]) <= ord('z'))
        offset = (1 << 5) if is_lower else 0
        print('{:c}'.format(ord(str[i]) - offset), end='')
    print('')
