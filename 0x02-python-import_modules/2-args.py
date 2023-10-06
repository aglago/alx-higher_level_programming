#!/usr/bin/python3

# AUTHOR - Ami Manye

# print argv and argc
if __name__ == '__main__':
    import sys

    '''print number of arguments'''
    if len(sys.argv) == 1:
        print('{} arguments.'.format(0))
    elif len(sys.argv) == 2:
        print('{} argument:'.format(1))
    else:
        print('{} arguments:'.format(len(sys.argv) - 1))

    '''print argument values'''
    i = 1
    while i < len(sys.argv):
        print('{}: {}'.format(i, sys.argv[i]))
        i += 1
