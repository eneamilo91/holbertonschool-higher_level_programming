#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        res = 1
        for i in range(b):
            res *= a
        return res
    else:
        res = 1
        for i in range(-b):
            res *= (1/a)
        return res
