#!/usr/bin/python3
"""This script defines a class called MagicClass that matches a specific bytecode provided by Holberton."""

import math

class MagicClass:
    """This class represents a circle."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass instance.

        Args:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
