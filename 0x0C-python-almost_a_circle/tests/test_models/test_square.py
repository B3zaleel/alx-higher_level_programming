#!/usr/bin/python3
"""A unit test module for the polygon models.
"""
from io import StringIO
import unittest
from unittest.mock import patch
from importlib import import_module


Base = import_module('.base', package='models').Base
Rectangle = import_module('.rectangle', package='models').Rectangle
Square = import_module('.square', package='models').Square


class TestSquare(unittest.TestCase):
    """Tests the Square class and its methods.
    """

    def test_init(self):
        """Tests the initialization of the Square class.
        """
        polygon = Square(5)
        id_init = polygon.id
        self.assertIsInstance(polygon, Base)
        self.assertIsInstance(polygon, Rectangle)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square('10')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square('10', 23)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, '20')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, 20, '25')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(0)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(-6)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(6, -3)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(6, 3, -7)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        with self.assertRaises(AttributeError):
            polygon.__nb_objects += 1
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, 13, 3, 7, 12)
