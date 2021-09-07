#!/usr/bin/python3
def uppercase(str):
    '''
    Prints a string, converting lowercase characters to uppercase

    Parameters:
    str (str): The string to print
    '''
    for i in range(len(str)):
        is_lower = ((ord(str[i]) >= ord('a')) and (ord(str[i]) <= ord('z')))
        print('{:c}{:s}'.format(
            ((ord(str[i]) - (1 << 5)) * is_lower),
            (str[i] * (not is_lower))
            ), end=('\n' * (i == (len(str) - 1))))

# uppercase('')
# uppercase("holberton")
# uppercase("holbert &^*= on")
# uppercase("Holberton School 98 Battery street")
