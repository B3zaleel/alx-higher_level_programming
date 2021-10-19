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
        """Tests the initialization of the Rectangle class.
        """
        self.assertIsInstance(Rectangle(5, 8), Base)
        self.assertEqual(Rectangle(5, 8).width, 5)
        self.assertEqual(Rectangle(5, 8).height, 8)
        self.assertEqual(Rectangle(5, 8, 0, 0).x, 0)
        self.assertEqual(Rectangle(5, 8, 0, 0).y, 0)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle('10', 13)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(None, 13)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(True, 13)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, '13')
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, None)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, True)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, '20')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, None)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, True)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, 20, '25')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, 20, None)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, 20, True)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(0, 13)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(-10, 13)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(10, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(10, -13)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(6, 9, -3)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(6, 9, 3, -7)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, 3, 7, 1, 12)

    def test_attribute_validation(self):
        """Tests the validation of attribute and instantiation.
        """
        polygon = Rectangle(5, 3)
        # region the width attribute
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).width = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).width = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).width = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).width = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).width = None
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).width = False
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).width = True
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(OverflowError):
            Rectangle(5, 3).width = int(float('inf'))
        with self.assertRaises(OverflowError):
            Rectangle(5, 3).width = int(float('-inf'))
        with self.assertRaises(ValueError):
            Rectangle(5, 3).width = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            Rectangle(5, 3).width = 0
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            Rectangle(5, 3).width = -5
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        # endregion
        # region the height attribute
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).height = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).height = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).height = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).height = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).height = None
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).height = False
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).height = True
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(OverflowError):
            Rectangle(5, 3).height = int(float('inf'))
        with self.assertRaises(OverflowError):
            Rectangle(5, 3).height = int(float('-inf'))
        with self.assertRaises(ValueError):
            Rectangle(5, 3).height = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            Rectangle(5, 3).height = 0
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            Rectangle(5, 3).height = -5
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        # endregion
        # region the x attribute
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).x = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).x = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).x = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).x = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).x = None
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).x = False
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).x = True
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(OverflowError):
            Rectangle(5, 3).x = int(float('inf'))
        with self.assertRaises(OverflowError):
            Rectangle(5, 3).x = int(float('-inf'))
        with self.assertRaises(ValueError):
            Rectangle(5, 3).x = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            Rectangle(5, 3).x = -5
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        # endregion
        # region the y attribute
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).y = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).y = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).y = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).y = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).y = None
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).y = False
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            Rectangle(5, 3).y = True
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(OverflowError):
            Rectangle(5, 3).y = int(float('inf'))
        with self.assertRaises(OverflowError):
            Rectangle(5, 3).y = int(float('-inf'))
        with self.assertRaises(ValueError):
            Rectangle(5, 3).y = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            Rectangle(5, 3).y = -5
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        # endregion

    def test_area(self):
        """Tests the area method of this polygon.
        """
        polygon = Rectangle(12, 3)
        self.assertEqual(Rectangle(12, 3).area(), 12 * 3)
        self.assertEqual(Rectangle(5, 2).area(), 5 * 2)
        self.assertEqual(Rectangle(10, 10, 60, 45, 3).area(), 10 * 10)
        self.assertEqual(Rectangle(10, 10, 60, 45).area(), 10 * 10)
        self.assertEqual(Rectangle(10, 10, 60).area(), 10 * 10)
        with self.assertRaises(TypeError):
            Rectangle(5, 3).area(None)
        with self.assertRaises(TypeError):
            Rectangle(5, 3).area(False)
        with self.assertRaises(TypeError):
            Rectangle(5, 3).area(12)
        with self.assertRaises(TypeError):
            Rectangle(5, 3).area(10, 10)
        with self.assertRaises(TypeError):
            Rectangle(5, 3).area((10, 10))
