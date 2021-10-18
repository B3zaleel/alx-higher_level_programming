#!/usr/bin/python3
"""A unit test module for the polygon models.
"""
import os
import unittest
import json
from importlib import import_module


Base = import_module('.base', package='models').Base
Rectangle = import_module('.rectangle', package='models').Rectangle
Square = import_module('.square', package='models').Square


def remove_files():
    """Removes the serialized polygon object files
    from the current working directory.
    """
    if os.path.isfile('Base.json'):
        os.unlink('Base.json')
    if os.path.isfile('Rectangle.json'):
        os.unlink('Rectangle.json')
    if os.path.isfile('Square.json'):
        os.unlink('Square.json')
    if os.path.isfile('Base.csv'):
        os.unlink('Base.csv')
    if os.path.isfile('Rectangle.csv'):
        os.unlink('Rectangle.csv')
    if os.path.isfile('Square.csv'):
        os.unlink('Square.csv')


def read_text_file(file_name):
    """Reads the contents of a given file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The contents of the file if it exists.
    """
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)
    return ''.join(lines)


class TestBase(unittest.TestCase):
    """Tests the Base class and its methods.
    """

    def test_init(self):
        """Tests the initialization of the Base class.
        """
        polygon = Base()
        id_init = polygon.id
        polygon = Base()
        self.assertEqual(polygon.id, id_init + 1)
        polygon = Base('0x10')
        self.assertEqual(polygon.id, '0x10')
        polygon = Base()
        self.assertEqual(polygon.id, id_init + 2)
        polygon = Base([1, 5])
        self.assertListEqual(polygon.id, [1, 5])
        polygon = Base()
        self.assertEqual(polygon.id, id_init + 3)
        polygon = Base(None)
        self.assertIsNotNone(polygon.id)
        self.assertEqual(polygon.id, id_init + 4)
        polygon = Base(False)
        self.assertEqual(polygon.id, False)
        polygon = Base(True)
        self.assertEqual(polygon.id, True)
        with self.assertRaises(AttributeError):
            polygon.__nb_objects += 1
        with self.assertRaises(TypeError):
            polygon = Base(1, 2)
