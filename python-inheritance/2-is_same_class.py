#!/usr/bin/python3

"""Module that holds a function"""


def is_same_class(obj, a_class):
    """Func to verify accordance"""
    if isinstance(obj, a_class):
        return True
    return False
