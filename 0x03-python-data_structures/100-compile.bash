#!/bin/bash
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.8 100-print_python_list_info.c
[ $? -eq 0 ] && ./100-test_lists.py
