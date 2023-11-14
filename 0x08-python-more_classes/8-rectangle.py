#!/usr/bin/python3

# AUTHOR - Ami Manye

'''represents a Rectangle class'''


class Rectangle:
    '''defines a rectangle'''

    # class attributes

    number_of_instances = 0
    print_symbol = '#'

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

        Rectangle.number_of_instances += 1

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

    # public methods

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
        if self.__width == 0 or self.__height == 0:
            return ''

        rect = ''

        for i in range(self.__height):
            rect += str(self.print_symbol) * self.__width + '\n'
        return rect[:-1]

    def __repr__(self):
        '''returns a string representation of the object'''
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        '''this function gets called when del is called on an object'''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    def bigger_or_equal(rect_1, rect_2):
        '''
        Which rectangle is larger ?

        Parameters:
        - rect_1 (Rectangle): The first rectangle
        - rect_2 (Rectangle): The second rectangle

        Returns:
        Rectangle: The rectangle object which is larger
        '''
        # checking the type of passed arguments
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        # comparing and returning the largest
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
