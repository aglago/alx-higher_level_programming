#!/usr/bin/python3

# AUTHOR - Ami Manye

def safe_print_division(a, b):
    """function that divides 2 integers and prints the results"""
    div = None
    try:
        div = a / b
    except Exception:
        return
    finally:
        if div is not None:
            print('Inside result: {:f}'.format(div))
    return div
