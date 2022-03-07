#!/usr/bin/python3
"""
Module for unittest Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Unittest Base class
    """
    @classmethod
    def setUpClass(cls):
        cls.base1 = Base()

    def test_id(self):
        self.assertEqual(self.base1.id, 1)

    def test_nb_objects(self):
        self.assertEqual(ase.__nb_objects, 1)
