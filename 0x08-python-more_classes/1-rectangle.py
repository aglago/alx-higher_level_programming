#!/usr/bin/python3

# AUTHOR - Ami Manye

'''represents a Rectangle class'''


class Rectangle:
    '''defines a rectangle'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''getter function: property'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter function'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif self.__width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''getter function: property'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter function'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif self.__height < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
