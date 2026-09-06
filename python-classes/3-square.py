#!/usr/bin/python3
"""
Module that defines a Square class with size validation and area computation.
"""


class Square:
    """
    Class that defines a square with a private size attribute.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size: The size of the square (must be an integer >= 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            The current square area.
        """
        return self.__size * self.__size
