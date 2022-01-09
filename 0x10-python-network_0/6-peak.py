#!/usr/bin/python3
"""Algorithms for list of integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not isinstance(list_of_integers, list) or len(list_of_integers) == 0:
        return None
    else:
        sorted_list = list_of_integers.sort()
        return sorted_list[len(sorted_list) - 1]
