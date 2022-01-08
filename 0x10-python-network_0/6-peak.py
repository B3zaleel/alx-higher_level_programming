#!/usr/bin/python3
"""Algorithms for list of integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not isinstance(list_of_integers, list) or len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        if list_of_integers[1] > list_of_integers[0]:
            return list_of_integers[1]
        else:
            return list_of_integers[1]
    else:
        n = len(list_of_integers)
        mid = n // 2
        if list_of_integers[mid] < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[0:mid - 1])
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            return find_peak(list_of_integers[mid + 1:n])
        else:
            return list_of_integers[mid]
