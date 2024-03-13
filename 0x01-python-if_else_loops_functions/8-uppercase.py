#!/usr/bin/python3

def uppercase(str):
    result = ""
    for s in str:
        if 'a' <= s <= 'z':
            result += chr(ord(s) - 32)
        else:
            result += s
    return "{}".format(result)
