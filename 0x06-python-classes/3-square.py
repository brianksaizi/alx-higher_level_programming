#!/usr/bin/python3
"""This script defines a class called Square."""

class Square:
    """This class represents a geometric square."""

    def __init__(self, size=0):
        """Initialize a new square instance.

        Args:
            size (int): The size of the new square.
        
        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the current area of the square."""
        return self.__size * self.__size
