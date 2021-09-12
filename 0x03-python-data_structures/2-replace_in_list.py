#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''
    Replaces an element of a list at a given index

    Parameters:
    my_list (lust): The list to modify
    idx (int): The index of the item to replace
    element (int): The item to be used as a replacement

    Return:
    The modified list
    '''
    if idx < len(my_list) and idx >= 0:
        my_list[idx] = element
    return my_list
