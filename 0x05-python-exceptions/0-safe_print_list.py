#!/usr/bin/python3
'''
print a list of items in a list
'''
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list[:x]:
            print(i, end='')
            count += 1
        print()
    except IndexError:
        print()
        return count
    return count
