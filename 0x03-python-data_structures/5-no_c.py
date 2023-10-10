#!/usr/bin/python3

# AUTHOR - Ami Manye

def no_c(my_string):
    '''remove all c and C from my_string'''

    new_string = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            new_string += c
    return (new_string)
