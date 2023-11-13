#!/usr/bin/python3

# AUTHOR : AMI MANYE

'''Defining test cases to test public methods of the Rectangle class'''


# importing the necessary models
import unittest
from unittest.mock import patch
import io
from models.rectangle import Rectangle

# test class begins
class TestPublicMethodsRectangle(unittest.TestCase):
    '''Representing a test public method blueprint'''

    # testing area
    def test_area(self):
        '''testing for rectangle area'''

        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)


    # testing display
    def test_display(self):
        '''testing for drawing rectangle with #'''
        
        r = Rectangle(2, 5)
        with patch('sys.stdout', new_callable=io.StringIO) as captured:
            r.display()
            expected_output = '##\n##\n##\n##\n##\n'
            self.assertEqual(expected_output, captured.getvalue())

    # testing display considering x and y
    def test_display_xy(self):
        '''printing the rectangle with # considering the values of x and y'''
        r = Rectangle(2, 3, 2, 2)

        with patch('sys.stdout', new_callable=io.StringIO) as captured:
            r.display()

            expected = '\n\n  ##\n  ##\n  ##\n'
            self.assertEqual(expected, captured.getvalue())

    def test_display_xy_2(self):
        '''test 2: printing rectangle considering x and y values'''
        r = Rectangle(3, 2, 1, 0)
        
        with patch('sys.stdout', new_callable=io.StringIO) as captured:
            r.display()

            expected = ' ###\n ###\n'
            self.assertEqual(expected, captured.getvalue())


    # testing display with incorrect initializing input
    def test_display_incorrect(self):
        '''testing with incorrect class initialization input'''

        r = Rectangle(3, 1, 0, 1)
        with patch('sys.stdout', new_callable=io.StringIO) as captured:
            r.display()

            expected_output = '###\n'
            self.assertEqual(expected_output, captured.getvalue())


if __name__ == '__main__':
    unittest.main()
