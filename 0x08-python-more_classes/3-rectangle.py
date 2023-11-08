#!/usr/bin/python3

# AUTHOR - Ami Manye

'''represents a Rectangle class'''


class Rectangle:
    '''defines a rectangle'''
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
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
        elif value < 0:
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
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''defines area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''defines perimeter of the rectangle'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        '''defines a string representation of the rectangle'''
        rect = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect += '#'
            if i < self.__height - 1:
                rect += '\n'
        #rect -= '\n'
        return rect
