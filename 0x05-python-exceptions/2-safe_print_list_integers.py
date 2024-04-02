#!/usr/bin/python3

'''
A function that prints the first x integers of a list.
'''
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if not isinstance(my_list[i], int):
                continue
            print("{:d}".format(i), end='')
            count += 1
        print()
    except ValueError:
        pass
    return count
