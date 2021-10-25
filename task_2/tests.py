""" Test for custom list """
import unittest as ut
from main import CustomList


class TestValidOut(ut.TestCase):
    """ Testing working custom list """
    def test_math(self):
        """ Testing math methods """
        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([-3, 0, 9])
        list3 = [4, 5, 6, 7, 8]
        self.assertEqual(list1 + list2, [-2, 2, 12, 4])
        self.assertEqual(list3 + list2, [1, 5, 15, 7, 8])
        self.assertEqual(list1 + list3, [5, 7, 9, 11, 8])
        self.assertEqual(list1 - list2, [4, 2, -6, 4])
        self.assertEqual(list2 - list3, [-7, -5, 3, -7, -8])

    def test_comparison(self):
        """ Testing comparisons """
        list1 = CustomList([1, 2, 3, 4])
        list2 = CustomList([-3, 0, 9])
        list3 = [4, 5, 6, 7, 8]
        self.assertTrue(list1 > list2)
        self.assertTrue(list3 > list1)
        self.assertTrue(list3 < [100])


if __name__ == '__main__':
    ut.main()
