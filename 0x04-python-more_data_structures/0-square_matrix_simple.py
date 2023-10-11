#!/usr/bin/python3

# AUTHOR - Ami Manye

def square_matrix_simple(matrix=[]):
    '''compute the square value of all integers of a matrix.'''

    '''create an empty matrix'''
    new_matrix = []
    '''work on each row using list comprehension'''
    for row in matrix:
        new_row = [elem**2 for elem in row]
        '''append new row to new matrix'''
        new_matrix.append(new_row)

    return new_matrix
