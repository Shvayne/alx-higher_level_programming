#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_num = abs(number)
mod = abs_num % 10
if (mod > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, mod))
if (mod == 0):
    print("Last digit of {} is {} and is 0".format(number, mod))
if (mod < 6 and mod != 0):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, mod))
