#!/usr/bin/python3
"""
Module that defines a Rectangle class with width, height, area, perimeter,
string representation using print_symbol, recreatable repr(), instance counter,
static comparison method, class square constructor, and destructor message.
"""


class Rectangle:
    """
    Class that defines a rectangle by width and height.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width: The width of the rectangle (must be an integer >= 0).
            height: The height of the rectangle (must be an integer >= 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        Args:
            value: The new width (must be an integer >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        Args:
            value: The new height (must be an integer >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Compute and return the area of the rectangle.

        Returns:
            The rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Compute and return the perimeter of the rectangle.

        Returns:
            The rectangle perimeter, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation of the rectangle using print_symbol.

        If width or height is 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        rect = []
        for _ in range(self.__height):
            rect.append(symbol * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """
        Return a string representation that can recreate the instance using eval().
        """
        return (
            f"Rectangle({self.__width}, {self.__height})"
        )

    def __del__(self):
        """
        Print a message when the rectangle instance is deleted and
        decrement the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on area.

        Args:
            rect_1: First rectangle (must be an instance of Rectangle).
            rect_2: Second rectangle (must be an instance of Rectangle).

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            The rectangle with the larger area, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Return a new Rectangle instance with width == height == size.

        Args:
            size: The size of the square sides (must be an integer >= 0).

        Returns:
            A new Rectangle instance representing a square.
        """
        return cls(size, size)
