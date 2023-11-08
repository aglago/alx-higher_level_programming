#!/usr/bin/python3

# AUTHOR - Ami Manye

'''represents a Rectangle class'''


class Rectangle:
    '''defines a rectangle'''
    def __init__(self, width=0, height=0):
        self.__width = width

    @property
    def width(self):
        '''getter function: property'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter function'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        '''getter function: property'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter function'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if self.__width < 0:
            raise ValueError('height must be >= 0')
