#!/usr/bin/python3

"""module about a rectangle"""
from models.base import Base


class Rectangle(Base):
    """class about a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """func to calculate area"""
        return self.__width * self.__height

    def display(self):
        """func to display the rectangle"""
        for y in range(self.y):
            print()
        for h in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """func to add args to object"""
        attributes = ["id", "width", "height", "x", "y"]
        if args and args is not None:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key in kwargs.keys():
                if key in attributes:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """func to return a dictionary"""
        return self.__dict__

    def to_dictionary(self):
        """func to print a dict representation """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
