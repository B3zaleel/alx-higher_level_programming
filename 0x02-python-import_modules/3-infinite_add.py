#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv_sum = 0
    for arg in sys.argv[1:]:
        argv_sum += int(arg)
    print('{:d}'.format(argv_sum))
