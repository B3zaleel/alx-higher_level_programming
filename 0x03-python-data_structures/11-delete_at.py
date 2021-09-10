#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    '''
    Removes the item at the given index in the given list

    Parameters:
    my_list (list): The list to modify
    idx (int): The index of the item to remove

    Return:
    The modified list
    '''
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
