#!/usr/bin/python3

# AUTHOR - Ami Manye

def safe_print_integer(value):
    """prints an integer with "{:d}".format()"""
    """returns true if integer and false if not"""

    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        return False
