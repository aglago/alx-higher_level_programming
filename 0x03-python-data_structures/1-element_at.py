#!/usr/bin/python3

# AUTHOR - Ami Manye

def element_at(my_list, idx):
    '''fetch element at index: idx'''

    '''if element is negative'''
    if idx < 0 or idx >= len(my_list):
        return

    '''print the element'''
    element = my_list[idx]
    return (element)
