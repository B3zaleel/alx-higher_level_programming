#!/usr/bin/python3
"""A unit test module for the polygon models.
"""
import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests the Base class and its methods.
    """

    @staticmethod
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

    @staticmethod
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

    def test_init(self):
        """Tests the initialization of the Base class.
        """
        self.assertFalse('nb_objects' in dir(Base))
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base().id, 4)
        self.assertEqual(Base(-10).id, -10)
        self.assertEqual(Base(10).id, 10)
        self.assertEqual(Base().id, 5)

    def test_to_json_string(self):
        """Tests the to_json_string method of the Base class.
        """
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{}]), '[{}]')
        self.assertEqual(Base.to_json_string([{'key': 'val'}]),
                         '[{"key": "val"}]')
