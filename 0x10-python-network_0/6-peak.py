#!/usr/bin/python3
""" Find a peak in the list of unsorted integers """

def find_peak(list_of_integers):
    """ Find a peak in the list of unsorted integers """
    if len(list_of_integers) <= 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]