#!/usr/bin/python3

# AUTHOR - Ami Manye

def print_reversed_list_integer(my_list=[]):
    '''print list passed in reverse order'''

    '''reverse'''
    my_list.reverse()

    '''print elements'''
    for elem in my_list:
        print('{}'.format(elem))
