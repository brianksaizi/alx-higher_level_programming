#!/usr/bin/python3
"""Define a function called raise_exception_msg to raise a NameError exception with a custom message."""

def raise_exception_msg(message=""):
    """Raise a NameError exception with a specified message.

    Args:
        message (str, optional): The custom error message to raise with the exception.
    """
    raise NameError(message)
