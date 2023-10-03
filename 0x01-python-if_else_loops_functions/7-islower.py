#!/usr/bin/python
def islower(c):
    for i in range(97, 123):
        if '{:c}'.format(i) == c:
            return True
    return False
