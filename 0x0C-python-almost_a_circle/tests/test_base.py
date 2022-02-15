#!/usr/bin/python3
"""
Module unittesting Base class
"""
import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Unittest Base class
    """
    def test_pep8_base(self):
        """
        unittest pep8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(check.total_errors, 0, "Found code style errors (and\
                         warnings).")

    def test_id_as_positive(self):
        """
        Unittest positive id
        """
        base_instance = Base(115)
        self.assertEqual(base_instance.id, 115)
        base_instance = Base(67)
        self.assertEqual(base_instance.id, 67)

    def test_id_as_negative(self):
        """
        Unittest negative id
        """
        base_instance = Base(-91)
        self.assertEqual(base_instance.id, -91)
        base_instance = Base(-4)
        self.assertEqual(base_instance.id, -4)

    def test_id_as_none(self):
        """
        Unittest none id
        """
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_string_id(self):
        """
        Unittest string id
        """
        base_instance = Base('Monty Python')
        self.assertEqual(base_instance.id, 'Monty Python')
        base_instance = Base('Python is cool')
        self.assertEqual(base_instance.id, 'Python is cool')

    def test_to_json_string(self):
        """
        Unittest to_json_string
        """
        rect_instance = Rectangle(10, 7, 2, 8, 70)
        rect_data = re1.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertEqual(type(json_data), str)

    def test_empty_to_json_string(self):
        """
        Unittest empty to_json_string
        """
        empty_data = []
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")
        empty_data = None
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

    def test_instance(self):
        """
        Unittest Base class instance
        """
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_to_json_string(self):
        """
        Unittest normal to_json_string
        """
        rect_data = {'id': 31, 'x': 14, 'y': 11, 'width': 3, 'height': 3}
        json_data = Base.to_json_string([rect_data])
        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(json_data, '{["id": 31, "x": 14, "y": 11,\
                              "width": 3, "height": 3]}')

    def test_wrong_to_json_string(self):
        """
        Unittest wrong to_json_string
        """
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")
        warn = ("to_json_string() missing 1 required positional argument: "\
                + "'list_dictionaries'")
        with self.assertRaises(TypeError) as msg:
            Base.to_json_string()
        self.assertEqual(warn, str(msg.exception))
        warn = "to_json_string() takes 1 positonal argument but 2 were given"
        with self.assertRaises(TypeError) as msg:
            Base.to_json_string([{43, 87}], [{22, 17}])
        self.assertEqual(warn, str(msg.exception))
