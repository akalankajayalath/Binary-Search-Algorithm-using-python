"""
This module focuses on unit testing of binary_search.py file
classes:SimpleTest
methods:testbasic1
"""
import unittest
from binary_search import binary_search_algo


class SimpleTest(unittest.TestCase):
    """
    This is the class that implements tests
    """
    def testBasic1(self):
        """
        unit testing happens in this method
        """
        self.assertEqual(binary_search_algo([], 2), False)#no value list
        self.assertEqual(binary_search_algo([1, 2, 5], 3), False)#value not in the list
        self.assertEqual(binary_search_algo([1, 2, 3, 4, 5], 1), True)#1st value of the list
        self.assertEqual(binary_search_algo([1, 2, 3, 4, 5], 13), True)#last value of the list
        self.assertEqual(binary_search_algo([1, 2, 3, 4, 5], 5), True)#middle value


if __name__ == '__main__':
    unittest.main()
