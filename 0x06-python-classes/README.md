# Classes and Objects

This project contains some tasks for learning about classes and objects in **Python**.

## Tasks To Complete

+ [x] 0\. My first square <br/>_**[0-square.py](0-square.py)**_  contains an empty class `Square` that defines a square.
+ [x] 1\. Square with size <br/>_**[1-square.py](1-square.py)**_  contains a class `Square` that defines a square by: (based on [`0-square.py`](0-square.py)).
  + Private instance attribute: `size`.
  + Instantiation with `size` (no type/value verification).
+ [x] 2\. Size validation <br/>_**[2-square.py](2-square.py)**_  contains a class `Square` that defines a square by: (based on [`1-square.py`](1-square.py)).
  + Private instance attribute: `size`.
  + Instantiation with optional `size`: `def __init__(self, size=0):` (`size` must be a number and greater than or equal to 0).
+ [x] 3\. Area of a square <br/>_**[3-square.py](3-square.py)**_  contains a class `Square` that defines a square by: (based on [`2-square.py`](2-square.py)).
  + Private instance attribute: `size`.
  + Instantiation with optional `size`: `def __init__(self, size=0):` (`size` must be a number and greater than or equal to 0).
  + Public instance method: `def area(self):` that returns the current square area.
+ [x] 4\. Access and update private attribute <br/>_**[4-square.py](4-square.py)**_  contains a class `Square` that defines a square by: (based on [`3-square.py`](3-square.py)).
  + Private instance attribute: `size`.
     + Property `def size(self):` to retrieve it.
     + Property setter `def size(self, value):` to set it (`size` must be a number and greater than or equal to 0).
  + Instantiation with optional `size`: `def __init__(self, size=0):`.
  + Public instance method: `def area(self):` that returns the current square area.
+ [x] 5\. Printing a square <br/>_**[5-square.py](5-square.py)**_  contains a class `Square` that defines a square by: (based on [`4-square.py`](4-square.py)).
  + Private instance attribute: `size`.
     + Property `def size(self):` to retrieve it.
     + Property setter `def size(self, value):` to set it (`size` must be a number and greater than or equal to 0).
  + Instantiation with optional `size`: `def __init__(self, size=0):`.
  + Public instance method: `def area(self):` that returns the current square area.
  + Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`. If `size` is equal to 0, print an empty line.
+ [x] 6\. Coordinates of a square <br/>_**[6-square.py](6-square.py)**_  contains a class `Square` that defines a square by: (based on [`5-square.py`](5-square.py)).
  + Private instance attribute: `size`.
     + Property `def size(self):` to retrieve it.
     + Property setter `def size(self, value):` to set it (`size` must be a number and greater than or equal to 0).
  + Private instance attribute: `position`.
     + Property `def position(self):` to retrieve it.
     + Property setter `def position(self, value):` to set it (`position` must be a tuple of 2 positive integers).
  + Instantiation with optional `size` and `position`: `def __init__(self, size=0, position=(0,0)):`.
  + Public instance method: `def area(self):` that returns the current square area.
  + Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`. If `size` is equal to 0, print an empty line. `position` should be used by using space - **Don’t fill lines by spaces** when `position[1] > 0`.
+ [x] 7\. Singly linked list <br/>_**[100-singly_linked_list.py](100-singly_linked_list.py)**_  contains a class `Node` that defines a node of a singly linked list by:
  + Private instance attribute: `data`.
     + Property `def data(self):` to retrieve it.
     + Property setter `def data(self, value):` to set it (`data` must be an integer).
  + Private instance attribute: `next_node`.
     + Property `def next_node(self):` to retrieve it.
     + Property setter `def next_node(self, value):` to set it (`next_node` can be `Node` or it must be a `Node`).
  + Instantiation with `data` and `next_node`: `def __init__(self, data, next_node=None):`.
  And, write a class `SinglyLinkedList` that defines a singly linked list by:
    + Private instance attribute: `head` (no setter or getter).
    + Simple instantiation: `def __init__(self):`.
    + Should be printable: Print the entire list in stdout, one node number per line.
    + Public instance method: `def sorted_insert(self, value):` that inserts a new `Node` into the correct sorted position in the list (increasing order).
+ [x] 8\. Print Square instance <br/>_**[101-square.py](101-square.py)**_  contains a class `Square` that defines a square by: (based on [`6-square.py`](6-square.py)).
  + Private instance attribute: `size`.
     + Property `def size(self):` to retrieve it.
     + Property setter `def size(self, value):` to set it (`size` must be a number and greater than or equal to 0).
  + Instantiation with optional `size` and `position`: `def __init__(self, size=0, position=(0,0)):`.
  + Public instance method: `def area(self):` that returns the current square area.
  + Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`. If `size` is equal to 0, print an empty line. `position` should be used by using space.
  + Printing a Square instance should have the same behavior as `my_print()`.
+ [x] 9\. Compare 2 squares <br/>_**[102-square.py](102-square.py)**_  contains a class `Square` that defines a square by: (based on [`4-square.py`](4-square.py)).
  + Private instance attribute: `size`.
     + Property `def size(self):` to retrieve it.
     + Property setter `def size(self, value):` to set it (`size` must be a number and greater than or equal to 0).
  + Instantiation with `size`: `def __init__(self, size=0):`.
  + Public instance method: `def area(self):` that returns the current square area.
  + `Square` instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<` and `<=` based on the square area.
+ [x] 10\. ByteCode -> Python #5 <br/>_**[103-magic_class.py](103-magic_class.py)**_ contains a Python class `MagicClass` that does exactly the same as the following Python bytecode:
  ```c
  Disassembly of __init__:
   10           0 LOAD_CONST               1 (0)
                3 LOAD_FAST                0 (self)
                6 STORE_ATTR               0 (_MagicClass__radius)

   11           9 LOAD_GLOBAL              1 (type)
               12 LOAD_FAST                1 (radius)
               15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
               18 LOAD_GLOBAL              2 (int)
               21 COMPARE_OP               9 (is not)
               24 POP_JUMP_IF_FALSE       60
               27 LOAD_GLOBAL              1 (type)
               30 LOAD_FAST                1 (radius)
               33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
               36 LOAD_GLOBAL              3 (float)
               39 COMPARE_OP               9 (is not)
               42 POP_JUMP_IF_FALSE       60

   12          45 LOAD_GLOBAL              4 (TypeError)
               48 LOAD_CONST               2 ('radius must be a number')
               51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
               54 RAISE_VARARGS            1
               57 JUMP_FORWARD             0 (to 60)

   13     >>   60 LOAD_FAST                1 (radius)
               63 LOAD_FAST                0 (self)
               66 STORE_ATTR               0 (_MagicClass__radius)
               69 LOAD_CONST               3 (None)
               72 RETURN_VALUE

  Disassembly of area:
   17           0 LOAD_FAST                0 (self)
                3 LOAD_ATTR                0 (_MagicClass__radius)
                6 LOAD_CONST               1 (2)
                9 BINARY_POWER
               10 LOAD_GLOBAL              1 (math)
               13 LOAD_ATTR                2 (pi)
               16 BINARY_MULTIPLY
               17 RETURN_VALUE

  Disassembly of circumference:
   21           0 LOAD_CONST               1 (2)
                3 LOAD_GLOBAL              0 (math)
                6 LOAD_ATTR                1 (pi)
                9 BINARY_MULTIPLY
               10 LOAD_FAST                0 (self)
               13 LOAD_ATTR                2 (_MagicClass__radius)
               16 BINARY_MULTIPLY
               17 RETURN_VALUE
  ```
