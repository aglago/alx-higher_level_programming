#!/usr/bin/python3

# AUTHOR - Ami Manye

'''A Square class'''


class Square:
    '''Represents a Square'''

    '''constructor for square class'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        '''getter function for size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''setter function for size'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if (self.__size < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''returns the area of the square'''
        res = self.__size ** 2
        return res

    def my_print(self):
        '''printing a number of #'''
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for i in range(self.__size):
                print('#', end='')
            print()
