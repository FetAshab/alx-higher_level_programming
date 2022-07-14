#!/usr/bin/python3
"""
Definning a Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Representing a Square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializing a new Square.
        Argumments:
            size (int): Size of Square.
            x    (int): X Square's coordinate.
            y    (int): Y Square's coordinate.
            id   (int): Square's identify.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getting Square's size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setting Square's size.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Square's update class.
        Argumments:
             *args   (ints): New attribute values.
                1st arg: means id attribute.
                2nd arg: means size attribute.
                3rd arg: means x coordinate atribute.
                4th arg: means y coordinate attribute.
            **kwargs (dict): Key/Value pair of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary.
         """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return a Standard print().
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
