# Conditionals, Loops and Functions

This project contains some tasks for learning about conditionals, loops, and functions in **Python**.

## Tasks To Complete

+ [x] 0\. Positive anything is better than negative nothing <br/>_**[0-positive_or_negative.py](0-positive_or_negative.py)**_ contains a Python script that will assign a random signed number to the variable `number` each time it is executed and print whether the number stored in the variable `number` is zero, positive or negative.
+ [x] 1\. The last digit <br/>_**[1-last_digit.py](1-last_digit.py)**_ contains a Python script that will assign a random signed number to the variable `number` each time it is executed and print the last digit of the number stored in the variable `number`.
+ [x] 2\. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game <br/>_**[2-print_alphabet.py](2-print_alphabet.py)**_ contains a Python script that prints the ASCII alphabet, in lowercase, not followed by a new line.
+ [x] 3\. When I was having that alphabet soup, I never thought that it would pay off <br/>_**[3-print_alphabt.py](3-print_alphabt.py)**_ contains a Python script that prints the ASCII alphabet (except `q` and `e`), in lowercase, not followed by a new line.
+ [x] 4\. Hexadecimal printing <br/>_**[4-print_hexa.py](4-print_hexa.py)**_ contains a Python script that prints all numbers from `0` to `98` in decimal and in hexadecimal (format: `dec = hex`, e.g.; `2 = 0x2`).
+ [x] 5\. 00...99 <br/>_**[5-print_comb2.py](5-print_comb2.py)**_ contains a Python script that prints numbers from `0` to `99` separated by a space and a comma and with a width of 2.
+ [x] 6\. Inventing is a combination of brains and materials. The more brains you use, the less material you need <br/>_**[6-print_comb3.py](6-print_comb3.py)**_ contains a Python script that prints all possible different combinations of two digits.
+ [x] 7\. islower <br/>_**[7-islower.py](7-islower.py)**_ contains a function that checks for lowercase character.
+ [x] 8\. To uppercase <br/>_**[8-uppercase.py](8-uppercase.py)**_ contains a function that prints a string in uppercase followed by a new line.
+ [x] 9\. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important <br/>_**[9-print_last_digit.py](9-print_last_digit.py)**_ contains a function that prints the last digit of a number.
+ [x] 10\. a + b <br/>_**[10-add.py](10-add.py)**_ contains a function that adds two integers and returns the result.
+ [x] 11\. a ^ b <br/>_**[11-pow.py](11-pow.py)**_ contains a function that computes `a` to the power of `b` and return the value.
+ [x] 12\. Fizz Buzz <br/>_**[12-fizzbuzz.py](12-fizzbuzz.py)**_ contains a function that prints the numbers from 1 to 100 separated by a space.
+ [x] 13\. Insert in sorted linked list <br/>_**[13-insert_number.c](13-insert_number.c)**_ contains a function in C that inserts a number into a sorted singly linked list.
+ [x] 14\. Smile in the mirror <br/>_**[100-print_tebahpla.py](100-print_tebahpla.py)**_ contains a Python script that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.
+ [x] 15\. Remove at position <br/>_**[101-remove_char_at.py](101-remove_char_at.py)**_ contains a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”).
+ [x] 16\. ByteCode -> Python #2 <br/>_**[102-magic_calculation.py](102-magic_calculation.py)**_ contains a function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:
  ```c
    3           0 LOAD_FAST                0 (a)
                3 LOAD_FAST                1 (b)
                6 COMPARE_OP               0 (<)
                9 POP_JUMP_IF_FALSE       16

    4          12 LOAD_FAST                2 (c)
               15 RETURN_VALUE

    5     >>   16 LOAD_FAST                2 (c)
               19 LOAD_FAST                1 (b)
               22 COMPARE_OP               4 (>)
               25 POP_JUMP_IF_FALSE       36

    6          28 LOAD_FAST                0 (a)
               31 LOAD_FAST                1 (b)
               34 BINARY_ADD
               35 RETURN_VALUE

    7     >>   36 LOAD_FAST                0 (a)
               39 LOAD_FAST                1 (b)
               42 BINARY_MULTIPLY
               43 LOAD_FAST                2 (c)
               46 BINARY_SUBTRACT
               47 RETURN_VALUE
  ```
