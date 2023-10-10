#!/usr/bin/python3

# AUTHOR - Ami Manye

def print_matrix_integer(matrix=[[]]):
    '''print matrix integer'''

    for int_list in matrix:
        for integer in int_list:
            print('{:d}'.format(integer), end=' ')
        print('')
