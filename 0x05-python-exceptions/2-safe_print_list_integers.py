#!/usr/bin/python3

# AUTHOR - Ami Manye

def safe_print_list_integers(my_list=[], x=0):
    """prints x elements of a list"""
    """returns real number of elements printed"""

    elements_printed = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[i]), end='')
            elements_printed += 1
        except (TypeError, ValueError):
            pass
    print()
    return elements_printed
