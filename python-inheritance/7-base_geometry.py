#!/usr/bin/python3

"""Module for a class"""


class BaseGeometry:
    """Class of basegeometry"""
    def area(self):
        """Func to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Func to validate int"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
