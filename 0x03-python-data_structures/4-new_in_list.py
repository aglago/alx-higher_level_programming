#!/usr/bin/python3

# AUTHOR - Ami Manye

def new_in_list(my_list, idx, element):
    '''replace element at idx without modifying my_list'''

    new_list = my_list.copy()

    '''if idx is negative or out of range'''
    if idx < 0 or idx >= len(my_list):
        return (new_list)

    new_list[idx] = element
    return (new_list)
