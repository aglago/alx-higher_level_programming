#/usr/bin/python3

# AUTHOR - Ami Manye

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    """returns real number of elements printed"""

    # if we should print nothing
    if x == 0:
        print()
        return 0

    # track elements printed
    elements_printed = 0;

    # iterate through list and print elements
    for element in my_list:
        try:
            print(f'{element}', end='')
            elements_printed += 1
        except exception as e:
            print(e)
        if elements_printed == x:
            print()
            return elements_printed
    print()
    return elements_printed
