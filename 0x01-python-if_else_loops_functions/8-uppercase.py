#!/usr/bin/python3
def uppercase(str):
    '''
    Prints a string, converting lowercase characters to uppercase

    Parameters:
    str (str): The string to print
    '''
    i = 0
    for c in str:
        is_lower = ((ord(c) >= ord('a')) and (ord(c) <= ord('z')))
        print('{:c}{:s}'.format(
            ((ord(c) - (1 << 5)) * is_lower),
            (c * (not is_lower))
            ), end=('\n' * (i == (len(str) - 1))))
        i += 1
