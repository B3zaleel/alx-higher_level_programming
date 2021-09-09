#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    a = 10
    b = 5
    funcs = [('+', add), ('-', sub), ('*', mul), ('/', div)]
    for func in funcs:
        print('{:d} {:s} {:d} = {:d}'.format(a, func[0], b, func[1](10, 5)))
