""" Test for this metaclass adding prefix "custom_" """
import unittest
from custom_meta import CustomMeta


class NewCustomClass(metaclass=CustomMeta):
    """ example class for testing """
    x = 50

    def __init__(self, val=99):
        """ initialization """
        self.val = val

    def line(self):
        """ return 100"""
        return 100


class TestMeta(unittest.TestCase):
    """ unit tests for custom metaclass """
    def setUp(self):
        """ set up example metaclass """
        self.inst = NewCustomClass()

    def test_attributes(self):
        """ test right write names """
        self.assertEqual(self.inst.custom_x, 50)
        with self.assertRaises(AttributeError):
            self.inst.x

        self.assertEqual(self.inst.custom_line(), 100)
        with self.assertRaises(AttributeError):
            self.inst.line()

        self.assertEqual(self.inst.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.inst.val
