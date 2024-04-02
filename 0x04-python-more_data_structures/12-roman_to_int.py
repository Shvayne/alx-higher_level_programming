#!/usr/bin/python3

def roman_to_int(roman_string):
    if not str(roman_string) or not roman_string:
        return 0
    roman_numerals = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
                      'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
                      'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    total = 0
    for char in roman_string:
        if char in roman_numerals:
            total += roman_numerals[char]
        else:
            return 0
    return total
