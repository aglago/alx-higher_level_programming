#!/usr/bin/python3

# AUTHOR - Ami Manye

def replace_in_list(my_list, idx, element):
    '''replace element at idx in my_list'''

    '''if element is negative'''
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    my_list[idx] = element

    return (my_list)
