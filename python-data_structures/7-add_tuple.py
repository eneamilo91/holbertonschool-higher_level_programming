#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        new_tuple.append(0)
        new_tuple.append(0)
    elif len(tuple_a) == 0 and len(tuple_b) == 1:
        new_tuple.append(tuple_b[0])
        new_tuple.append(0)
    elif len(tuple_a) == 1 and len(tuple_b) == 0:
        new_tuple.append(tuple_a[0])
        new_tuple.append(0)
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        new_tuple.append(tuple_a[0] + tuple_b[0])
        new_tuple.append(0)
    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        new_tuple.append(tuple_a[0])
        new_tuple.append(tuple_a[1])
    elif len(tuple_a) == 0 and len(tuple_b) == 2:
        new_tuple.append(tuple_b[0])
        new_tuple.append(tuple_b[1])
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        new_tuple.append(tuple_a[0] + tuple_b[0])
        new_tuple.append(tuple_a[1])
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        new_tuple.append(tuple_a[0] + tuple_b[0])
        new_tuple.append(tuple_b[1])
    else:
        new_tuple.append(tuple_a[0] + tuple_b[0])
        new_tuple.append(tuple_a[1] + tuple_b[1])
    new_tuple = tuple(new_tuple)
    return new_tuple
