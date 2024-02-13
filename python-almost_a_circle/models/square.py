#!/usr/bin/python3

"""module about a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class about a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=0, y=0, id=None)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        self.__size = value
