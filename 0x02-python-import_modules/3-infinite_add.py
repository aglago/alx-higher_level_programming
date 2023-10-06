#!/usr/bin/python3

# AUTHOR - Ami Manye

# add all arguments of argv (int)
if __name__ == '__main__':
    import sys

    '''loop through values and add'''
    sum = 0
    i = 1
    while i < len(sys.argv):
        sum += int(sys.argv[i])
        i += 1

    print('{}'.format(sum))
