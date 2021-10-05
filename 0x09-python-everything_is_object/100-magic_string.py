#!/usr/bin/python3
def magic_string():
    magic_string.c = magic_string.__dict__.get('c', 0) + 1
    return '{}{}'.format('BestSchool', ', BestSchool' * (magic_string.c - 1))
