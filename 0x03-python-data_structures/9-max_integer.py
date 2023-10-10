#!/usr/bin/python3

# AUTHOR - Ami Manye

def max_integer(my_list=[]):
    '''find the largest integer'''

    '''if list is empty'''
    if my_list is None or len(my_list) == 0:
        return

    largest = my_list[0]
    for num in my_list:
        if num > largest:
            largest = num
    return largest
