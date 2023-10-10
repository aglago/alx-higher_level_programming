#!/usr/bin/python3

# AUTHOR - Ami Manye

def delete_at(my_list=[], idx=0):
    '''delete item at specific position'''

    '''return nothing for negative index'''
    '''return nothing for out of range'''
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    lst = my_list.copy()
    return (lst)
