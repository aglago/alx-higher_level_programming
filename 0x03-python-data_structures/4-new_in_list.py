#!/usr/bin/python3

# AUTHOR - Ami Manye

def new_in_list(my_list, idx, element):
    '''replace element at idx without modifying my_list'''

    '''if list is None'''
    if my_list is None or idx < 0 or idx >= len(my_list):
        return;
    '''if idx is negative'''
    if idx < 0 or idx >= len(my_list):
        return (my_list.copy)
    '''if idx is out of range'''
    if my_list is None:
        return;

    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
