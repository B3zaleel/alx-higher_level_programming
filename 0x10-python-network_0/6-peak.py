#!/usr/bin/python3
"""Algorithms for list of integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers is None or not isinstance(list_of_integers, list):
        return None
    n = len(list_of_integers)
    peak = None
    for i in range(0, n, 1):
        cur = list_of_integers[i]
        prev = list_of_integers[i - 1] if i > 0 else None
        next = list_of_integers[i + 1] if i + 1 < n else None
        if prev is None:
            if next is None:
                peak = cur
        else:
            if next is None:
                if cur >= prev:
                    peak = cur
            else:
                if cur > prev and cur > next:
                    peak = cur
        if peak is not None:
            break
    return peak
