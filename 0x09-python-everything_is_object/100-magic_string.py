#!/usr/bin/python3
def magic_string():
    n = 0
    return ", ".join(["BestSchool" * i for i in range(1, n + 1)])

for i in range(10):
    print(magic_string())