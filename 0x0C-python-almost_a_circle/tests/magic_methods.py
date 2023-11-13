#!/usr/bin/python3

# AUTHOR : AMI MANYE

'''defining test cases for magic methods'''

import unittest
from models.rectangle import Rectangle

class TestMagicMethodsRectangle(unittest.TestCase):
    '''representing testcases'''

    def test__str__(self):
        '''testing the str() or print() calling of object'''
        r = Rectangle(4, 10, 1, 1, 12)

        expected_return = '[Rectangle] (12) 1/1 - 4/10'
        self.assertEqual(expected_return, str(r))

    def test__str__id(self):
        '''testing str() and print() when no initial id is given'''
        r = Rectangle(3, 4, 0, 1)
        
        expected_return = '[Rectangle] (1) 0/1 - 3/4'
        self.assertEqual(expected_return, str(r))

if __name__ == '__main__':
    unittest.main()
        
