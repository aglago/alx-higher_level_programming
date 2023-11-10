#!/usr/bin/python3

# AUTHOR - Ami Manye

'''defines a rectangle class'''


from models.base import Base

class Rectangle(Base):
    '''Represents a rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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

    @width.setter
    def width(self, value):
        '''setter function for width'''
        self.__width = value

    @height.setter
    def height(self, value):
        '''setter function for height'''
        self.__height = value

    @x.setter
    def x(self, value):
        '''setter function for x'''
        self.__x = value

    @y.setter
    def y(self, value):
        '''setter function for y'''
        self.__y = value
