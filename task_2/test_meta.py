""" Test for my metaclass adding prefix "custom_" """
import unittest
from custom_meta import CustomMeta


class NewCustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100


class TestMeta(unittest.TestCase):
    def setUp(self):
        self.inst = NewCustomClass()

    def test_attributes(self):

        self.assertEqual(self.inst.custom_x, 50)
        with self.assertRaises(AttributeError):
            self.inst.x

        self.assertEqual(self.inst.custom_line(), 100)
        with self.assertRaises(AttributeError):
            self.inst.line()

        self.assertEqual(self.inst.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.inst.val
