#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad both tuples to have at least 2 elements
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Use only the first two elements
    return (a[0] + b[0], a[1] + b[1])
