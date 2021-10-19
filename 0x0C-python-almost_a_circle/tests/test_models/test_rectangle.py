#!/usr/bin/python3
"""A unit test module for the polygon models.
"""
from io import StringIO
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class and its methods.
    """

    def test_init(self):
        """Tests the initialization of the Square class.
        """
        pass
        polygon = Rectangle(5, 8, 0, 0)
        id_init = polygon.id
        self.assertIsInstance(polygon, Base)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle('10', 13)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, '13')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, '20')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, 20, '25')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(0, 13)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(-10, 13)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(10, 0)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(10, -13)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(6, 9, -3)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(6, 9, 3, -7)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        with self.assertRaises(AttributeError):
            polygon.__nb_objects += 1
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, 3, 7, 1, 12)
