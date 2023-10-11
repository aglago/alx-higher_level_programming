#!/usr/bin/python3

# AUTHOR - Ami Manye

def uniq_add(my_list=[]):
    '''add all unique integers in a list (only once for each integer)'''

    new_list = list(set(my_list))
    sum = 0

    for elem in new_list:
        sum += elem
    '''result = reduce((lambda x,y:x+y), new_list)'''
    return sum
