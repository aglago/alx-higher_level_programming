#!/usr/bin/python3

# AUTHOR - Ami Manye

def multiple_returns(sentence):
    '''return tuple'''

    '''if sentence is empty'''
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]

    tup = (len(sentence), first_char)
    return (tup)
