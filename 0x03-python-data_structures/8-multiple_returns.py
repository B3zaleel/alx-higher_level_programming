#!/usr/bin/python3
def multiple_returns(sentence):
    '''
    Returns the length of a string and its first character

    Parameters:
    sentence (str): The given string

    Return:
    A tuple consisting of the length of the given string and its
    first character or None if the given string is empty
    '''
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
