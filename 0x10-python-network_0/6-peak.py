#!/usr/bin/python3
"""Algorithms for list of integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not isinstance(list_of_integers, list) or len(list_of_integers) == 0:
        return None
    else:
        n = len(list_of_integers)
        mid = n // 2
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[0 : mid - 1])
        elif mid + 1 < n and list_of_integers[mid] < list_of_integers[mid + 1]:
            return find_peak(list_of_integers[mid : n])
        else:
            return list_of_integers[mid]
