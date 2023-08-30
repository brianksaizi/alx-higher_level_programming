#!/usr/bin/python3
"""Define a function called safe_print_list_integers to safely print the first x integer elements from a list."""

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integer elements from a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print from my_list.

    Returns:
        int: The number of integer elements successfully printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return ret
