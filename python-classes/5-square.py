#!/usr/bin/python3
"""
Module that defines a Square class with size getter, setter, area computation,
and printing functionality.
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
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value: The new size (must be an integer >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            The current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the character '#'.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
