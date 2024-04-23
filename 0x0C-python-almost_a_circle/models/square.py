#!/usr/bin/python3
"""a square module"""
from rectangle import Rectangle
class Square(Rectangle):
    """Square class inheriting from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """consructor method
        Args:
            size: how big the square(int)
            x: dimensions(int)
            y: dimensions(int)
            """
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """pretty printing of a square instance"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """defines the length of a square"""
        return self.width
    
    @size.setter
    def size(self, value):
        """setter method for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes to the instance"""
        if args is not None and len(args) > 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = id
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
    

