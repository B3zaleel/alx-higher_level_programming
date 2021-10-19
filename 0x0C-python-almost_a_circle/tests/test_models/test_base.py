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
        id_init = Base().id
        self.assertEqual(id_init + 1, Base().id)
        self.assertEqual('0x10', Base('0x10').id)
        self.assertListEqual([1, 5], Base([1, 5]).id)
        self.assertIsNotNone(Base(None).id)
        self.assertNotEqual(None, Base(None).id)
        self.assertEqual(False, Base(False).id)
        self.assertEqual(True, Base(True).id)
        self.assertEqual(0, Base(0).id)
        self.assertEqual(-10, Base(-10).id)
        self.assertEqual(10, Base(10).id)
        self.assertFalse('nb_objects' in dir(Base))
        self.assertFalse('__nb_objects' in dir(Base))
        # with self.assertRaises(AttributeError):
        #     polygon.__nb_objects += 1
        # with self.assertRaises(AttributeError):
        #     polygon.nb_objects += 1
        with self.assertRaises(TypeError):
            polygon = Base(1, 2)
        with self.assertRaises(OverflowError):
            polygon = Base(int(float('inf')))

    def test_to_json_string(self):
        """Tests the to_json_string method of the Base class.
        """
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{}]), '[{}]')
        self.assertEqual(Base.to_json_string([{'x': 6}]), '[{"x": 6}]')

    def test_from_json_string(self):
        """Tests the from_json_string static method of the Base class.
        """
        self.assertEqual(Base.from_json_string('null'), None)
        self.assertEqual(Rectangle.from_json_string('34'), 34)
        self.assertEqual(Square.from_json_string('"foo_bar"'), 'foo_bar')
        self.assertEqual(Square.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Square.from_json_string('   '), [])
        self.assertEqual(Rectangle.from_json_string('   \n \t '), [])
        self.assertEqual(
            Base.from_json_string('[-4, 1, 2, 5]'),
            [-4, 1, 2, 5]
        )
        self.assertEqual(
            Rectangle.from_json_string(
                '[{"y": 8, "id": 89, "width": 10, "x": 4, "height": 4}]'
            ),
            [{'id': 89, 'width': 10, 'height': 4, 'x': 4, 'y': 8}]
        )
        self.assertEqual(
            Square.from_json_string(
                '[{"id": 98, "x": 15, "size": 30, "y": 10}]'
            ),
            [{'id': 98, 'size': 30, 'x': 15, 'y': 10}]
        )
        with self.assertRaises(TypeError):
            polygon_list = Base.from_json_string('[{"id": 45, "x": 3', '34')
        with self.assertRaises(TypeError):
            polygon_list = Base.from_json_string('[{"id": 45, "x": 3', None)
