#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    divider = 0

    for number1, number2 in my_list:
        total += number1 * number2
        divider += number2
    avg = total / divider
    return avg
