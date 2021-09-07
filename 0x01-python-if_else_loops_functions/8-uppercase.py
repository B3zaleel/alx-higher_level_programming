#!/usr/bin/python3
def uppercase(str):
    '''
    Prints a string, converting lowercase characters to uppercase

    Parameters:
    str (str): The string to print
    '''
    for i in range(len(str) + 1):
        c = 0
        if (len(str) > 0) and (i < len(str)):
            c = ord(str[i])
        is_lower = (c >= ord('a')) and (c <= ord('z'))
        offset = (1 << 5) if is_lower else 0
        end_str = '\n' if (len(str) == 0) or (i == (len(str) - 1)) else ''
        print('{:c}'.format(c - offset), end=end_str)
