#!/usr/bin/python3

# AUTHOR - Ami Manye
'''
prints numbers from 1 to 100
    for every multiple of 3, Fizz is printed
    for every multiple of 5, Buzz is printed
    for every multiple of both 3 and 5, FizzBuss is printed
    each element is followed by a space
'''


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=' ')
            continue
        elif i % 3 == 0:
            print('Fizz', end=' ')
            continue
        elif i % 5 == 0:
            print('Buzz', end=' ')
            continue
        else:
            print('{}'.format(i), end=' ')
