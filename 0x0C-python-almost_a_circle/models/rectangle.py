#!/usr/bin/python3

# AUTHOR - Ami Manye

'''defines a rectangle class'''


from models.base import Base

class Rectangle(Base):
    '''Represents a rectangle'''

    # init method

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        '''error checking for width'''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

        '''error checking for height'''
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

        '''error checking for x'''
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

        '''error checking for y'''
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    # properties

    @property
    def width(self):
        '''getter function for width'''
        return self.__width

    @property
    def height(self):
        '''getter function for height'''
        return self.__height

    @property
    def x(self):
        '''getter function for x'''
        return self.__x

    @property
    def y(self):
        '''getter function for y'''
        return self.__y

    # property setters

    @width.setter
    def width(self, value):
        '''setter function for width'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        '''setter function for height'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        '''setter function for x'''
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        '''setter function for y'''
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value


    # public methods

    def area(self):
        '''returns area of rectangle'''
        return self.__width * self.__height

    def display(self):
        '''prints in stdout the rectangle with character #'''
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            if i <= self.__height - 1:
                print()


    # magic methods

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'
