#!/usr/bin/python3
def uppercase(str):
    '''
    Prints a string, converting lowercase characters to uppercase

    Parameters:
    str (str): The string to print
    '''
    for i in range(len(str)):
        is_lower = (ord(str[i]) >= ord('a')) and (ord(str[i]) <= ord('z'))
        if is_lower:
            print('{:c}'.format(
                ord(str[i]) - (1 << 5)), end=('\n' * (i == (len(str) - 1))))
        else:
            print('{:s}'.format(
                str[i]
            ), end=('\n' * (i == (len(str) - 1))))
