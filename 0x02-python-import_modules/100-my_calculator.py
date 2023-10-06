#!/usr/bin/python3

# AUTHOR - Ami Manye

# import module
if __name__ == '__main__':
    from calculator_1 import add, sub, div, mul
    import sys

    '''print error if argv is not 3'''
    if len(sys.argv) - 1 != 3:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        exit(1)

    '''declaring variables'''
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    '''do operation'''
    if op == '+':
        print('{} {} {} = {}'.format(a, op, b, add(a,b)))
    elif op == '-':
        print('{} {} {} = {}'.format(a, op, b, sub(a,b)))
    elif op == '*':
        print('{} {} {} = {}'.format(a, op, b, mul(a,b)))
    elif op == '/':
        print('{} {} {} = {}'.format(a, op, b, sub(a,b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
