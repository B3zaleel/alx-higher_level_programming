#!/usr/bin/python3
def no_c(my_string):
    '''
    Removes all c and C characters from a given string

    Parameters:
    my_string (str): The given string to strip of c and C characters
    '''
    new_str = []
    for char in my_string:
        if char not in 'cC':
            new_str.append(char)
    return ''.join(new_str)
