#!/usr/bin/python3
"""a rectangle module"""
from base import Base
class Rectangle(Base):
    """A rectangle class
    Args:
        Base: parent class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    def __str__(self):
        """return the string representation of an instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
    

    @property
    def width(self):
        """defines the width of rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter method for width
        Args:
            value: value to set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """defines the height of rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter method for height
        args:
            value: value to set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """defines the dimensions of the triangle"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """setter method for x
        args:
            value to set it to
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method for y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """setter method for y
        args:
            value: the value to set y to
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width
    
    def display(self):
        """display a rectangle to stdout"""
        for y in range(self.y):
            print()
        for x in range(self.height):
            for x in range(self.x):
                print(" ", end='')
            print ("#" * self.__width)
        print()

    def update(self, *args, **kwargs):
        """Updates a rectangle's attributes"""
        if args and len(args) > 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
