#!/usr/bin/python3

# AUTHOR - Ami Manye

'''A Square class'''


class Square:
    '''This is a class with a private square attribute and public method'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return (self.__size ** 2)
