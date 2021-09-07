#!/usr/bin/python3
def uppercase(txt):
    '''
    Prints a string, converting lowercase characters to uppercase

    Parameters:
    txt (str): The string to print
    '''
    if isinstance(txt, str):
        for i in range(len(txt)):
            is_lower = (ord(txt[i]) >= ord('a')) and (ord(txt[i]) <= ord('z'))
            print('{:c}{:c}{:c}'.format(
                (ord(txt[i]) - (1 << 5)) * is_lower,
                ord(txt[i]) * (not is_lower),
                ord('\n') * (i == (len(txt) - 1))
                ), end='')
