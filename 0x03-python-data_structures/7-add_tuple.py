#!/usr/bin/python3

# AUTHOR - Ami Manye

def add_tuple(tuple_a=(), tuple_b=()):
    '''add tuples'''

    '''if tuple is none'''
    if len(tuple_a) < 2:
        tuple_a += 0,
        tuple_a += 0,
    if len(tuple_b) < 2:
        tuple_b += 0,
        tuple_b += 0,
    '''if tuple is 1'''
    if len(tuple_a) < 2:
        tuple_a += 0,
    if len(tuple_b) < 2:
        tuple_b += 0,

    '''if tuple is more than 2'''
    tup = ()
    tup += tuple_a[0] + tuple_b[0],
    tup += tuple_a[1] + tuple_b[1],

    return (tup)
    
