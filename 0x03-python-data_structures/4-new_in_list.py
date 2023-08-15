#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list

# Test cases
original_list = [1, 2, 3, 4, 5]
idx = 2
new_element = 10

modified_list = new_in_list(original_list, idx, new_element)
print("Original List:", original_list)
print("Modified List:", modified_list)
