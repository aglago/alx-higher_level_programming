#!/usr/bin/python3

# AUTHOR - Ami Manye

class Base:
    '''Representing a base'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
