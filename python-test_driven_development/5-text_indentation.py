#!/usr/bin/python3

"""Module to perform certain operations on a text"""


def text_indentation(text):
    """Func to perform such operations"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
        print(text[i], end="")
