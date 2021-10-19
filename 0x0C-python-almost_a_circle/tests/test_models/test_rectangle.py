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

    def test_attribute_validation(self):
        """Tests the validation of attribute and instantiation.
        """
        polygon = Rectangle(12, 3)
        # region the id
        polygon.id = 23
        self.assertEqual(polygon.id, 23)
        polygon.id = None
        self.assertEqual(polygon.id, None)
        polygon.id = False
        self.assertEqual(polygon.id, False)
        polygon.id = True
        self.assertEqual(polygon.id, True)
        polygon.id = 'foo'
        self.assertEqual(polygon.id, 'foo')
        # endregion
        # region the width attribute
        polygon.width = 12
        self.assertEqual(polygon.width, 12)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = None
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = False
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = True
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(OverflowError):
            polygon.width = int(float('inf'))
        with self.assertRaises(OverflowError):
            polygon.width = int(float('-inf'))
        with self.assertRaises(ValueError):
            polygon.width = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.width = 0
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.width = -5
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        # endregion
        # region the height attribute
        polygon.height = 12
        self.assertEqual(polygon.height, 12)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = None
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = False
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = True
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(OverflowError):
            polygon.height = int(float('inf'))
        with self.assertRaises(OverflowError):
            polygon.height = int(float('-inf'))
        with self.assertRaises(ValueError):
            polygon.height = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.height = 0
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.height = -5
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        # endregion
        # region the x attribute
        polygon.x = 12
        self.assertEqual(polygon.x, 12)
        polygon.x = 0
        self.assertEqual(polygon.x, 0)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = None
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = False
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = True
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(OverflowError):
            polygon.x = int(float('inf'))
        with self.assertRaises(OverflowError):
            polygon.x = int(float('-inf'))
        with self.assertRaises(ValueError):
            polygon.x = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.x = -5
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        # endregion
        # region the y attribute
        polygon.y = 12
        self.assertEqual(polygon.y, 12)
        polygon.y = 0
        self.assertEqual(polygon.y, 0)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = None
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = False
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = True
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(OverflowError):
            polygon.y = int(float('inf'))
        with self.assertRaises(OverflowError):
            polygon.y = int(float('-inf'))
        with self.assertRaises(ValueError):
            polygon.y = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.y = -5
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        # endregion
