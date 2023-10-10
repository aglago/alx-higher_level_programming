#!/usr/bin/python3

# AUTHOR - Ami Manye

def divisible_by_2(my_list=[]):
    '''check for divisibility by 2'''

    lst = []
    for num in my_list:
        if num % 2 == 0:
            lst.append(True)
        else:
            lst.append(False)
    return (lst)
