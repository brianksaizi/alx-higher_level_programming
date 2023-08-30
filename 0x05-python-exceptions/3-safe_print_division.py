#!/usr/bin/python3
"""Define a function called safe_print_division to safely perform division and print the result."""

def safe_print_division(a, b):
    """Perform division of a by b and print the result.

    Args:
        a (float or int): The numerator for the division.
        b (float or int): The denominator for the division.

    Returns:
        The result of the division, or None if division is not possible.
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
