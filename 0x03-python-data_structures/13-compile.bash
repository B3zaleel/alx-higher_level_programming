#!/bin/bash
gcc -Wall -Werror -Wextra -pedantic 13-test.c linked_lists.c 13-is_palindrome.c -o palindrome
[ $? -eq 0 ] && ./palindrome
[ $? -eq 0 ] && valgrind ./palindrome
