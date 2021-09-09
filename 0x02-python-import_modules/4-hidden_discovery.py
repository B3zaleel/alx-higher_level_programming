#!/usr/bin/python3
if __name__ == '__main__':
    from importlib import import_module
    hidden_4 = import_module('hidden_4')
    for name in dir(hidden_4):
        if not name.startswith('__'):
            print('{:s}'.format(name))
