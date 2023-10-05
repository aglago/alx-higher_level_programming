#!/usr/bin/python3

# AUTHOR - Ami Manye

# import function from another module
from add_0 import add
a = 1
b = 2

if __name__ == '__main__':
    print('{} + {} = {}'.format(a, b, add(a, b)))
