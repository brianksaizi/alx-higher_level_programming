#!/usr/bin/python3
# 2-replace_in_list.py


def replace_in_list(my_list, idx, element):
    """Substitute a list element at a particular position."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
