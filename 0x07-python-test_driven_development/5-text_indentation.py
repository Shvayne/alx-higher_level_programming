#!/usr/bin/python3
"""this module contains a function that formats text"""
def text_indentation(text):
    """formats a string
    Args:
        text (str): string to be formatted
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] ==  " ":
        i += 1
    while i < len(text):
        print(text[i], end='')
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
