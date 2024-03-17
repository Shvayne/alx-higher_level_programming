#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if isinstance(tuple_a, tuple):
        tuple_a = tuple_a[:2]
    else:
        tuple_a = (tuple_a, 0)
    if isinstance(tuple_b, tuple):
        tuple_b = tuple_b[:2]
    else:
        tuple_b = (tuple_b, 0)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_b[1] + tuple_a[1])
    return new_tuple
