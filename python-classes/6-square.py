#!/usr/bin/python3

"""module about a class in python"""


class Square:
    """the class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """func to initialize objects"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__position = position

    def area(self):
        """Method to calculate the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """getter of the property"""
        return self.__size

    @size.setter
    def size(self, value):
        """methd to set the value of an attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for a in range(self.size):
                for i in range(self.position[0]):
                    print(" ", end="")
                for b in range(self.size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """Method to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) is False or len(value) != 2
           or (isinstance(value[0], int) is False or value[0] < 0)
           or (isinstance(value[1], int) is False or value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
