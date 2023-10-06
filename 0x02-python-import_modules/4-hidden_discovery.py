#!/usr/bin/python3

# AUTHOR - Ami Manye

# prints all names defined by a compiled module
if __name__ == '__main__':
    import hidden_4

    '''print name(vars, functions, etc) which do not start with __'''
    for item in dir(hidden_4):
        if item[0] == '_' and item[1] == '_':
            continue
        else:
            print('{}'.format(item))
