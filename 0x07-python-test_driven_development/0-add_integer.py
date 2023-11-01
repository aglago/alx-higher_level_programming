#!/usr/bin/python3

# AUTHOR - Ami Manye

"""
This is a python module defines a function ```add_integer```
"""

def add_integer(a, b=98):
    """
    This function adds 2 numbers together

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    elif isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)

    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testfile('0_add_integer.txt')
