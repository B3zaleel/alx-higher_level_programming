#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''
    Creates a new list, replacing the item at the given
    index in the list with the given element

    Parameters:
    my_list (list): The list to create a copy of
    idx (int): The index of the item to replace
    element (int): The item to be used as a replacement

    Return:
    A copy of the given list
    '''
    new_list = []
    for i in range(len(my_list)):
        new_list.append(element if i == idx else my_list[i])
    return new_list
