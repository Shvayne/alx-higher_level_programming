#!/usr/bin/python3
"""this module contains a function that finds a peak in a list of integers"""

def find_peak(list_of_integers):
    """finds the peak in a list of ints"""
    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            #peak is in the left half
            right = mid
        else:
            #peak is in the right half
            left = mid + 1
    return list_of_integers[left]

