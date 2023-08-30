#!/usr/bin/python3
"""Define a function safe_print_list to safely print elements from a list."""

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        int: The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return ret
