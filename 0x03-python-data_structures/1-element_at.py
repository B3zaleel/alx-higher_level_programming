#!/usr/bin/python3
def element_at(my_list, idx):
    '''
    Retrieves the element at the given index in the given list

    Parameters:
    my_list (list): The list to retrieve the item from
    idx (int): The index of the item to retrieve

    Return:
    None if index is less than 0 or greater than or equal to the
    length of the given list, otherwise the item at the given index
    '''
    return None if idx < 0 or idx >= len(my_list) else my_list[idx]
