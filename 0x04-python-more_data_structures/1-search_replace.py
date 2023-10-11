#!/usr/bin/python3

# AUTHOR - Ami Manye

def search_replace(my_list, search, replace):
    '''replace all occurrences of an element by another in a new list'''

    new_list = [replace if elem == search else elem for elem in my_list]
    '''
    for elem in my_list:
        if elem == search:
            new_list.append(replace)
        else:
            new_list.append(elem)
    '''
    return new_list
