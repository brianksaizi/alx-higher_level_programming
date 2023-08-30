#!/usr/bin/python3
"""Define a function called safe_print_integer to safely print an integer using "{:d}".format()."""

def safe_print_integer(value):
    """Print an integer using "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if the integer is printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
