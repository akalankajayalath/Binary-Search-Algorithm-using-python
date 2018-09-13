"""
#module docstring
This program accepts a list from user and search for a given number
uses binary search algorithm.
Functions:
    binary_search(list_to_find_the_number,Number)
"""

import random

def sort_list(length):
    """
    inputs:
        @length:length of the list that want to be generated

    outputs:
        @generate_list:list that generated

    #function docstring
    creating the list as per the users required length
    """

    generate_list = []
    for _ in range(length):
        generate_list.append(random.randint(0, 100000))

    generate_list.sort()
    return generate_list




def binary_search_algo(s_list, s_number):

    """
    #function docstring
    inputs:
        @s_list:list that want to be used
        @s_number:Number that should be searched

    outputs:
        @num_found:True or False
    search for the given number in a list
    function is only accepting sorted lists
    """

    first = 0
    last = len(s_list) - 1
    num_found = False

    while last >= first and not num_found:
        mid_value = (first + last)//2

        if s_list[mid_value] == s_number:
            num_found = True
            break
        else:
            if s_number < s_list[mid_value]:
                last = mid_value - 1
            else:
                first = mid_value + 1

    return num_found


def get_inputs(print_msg):

    """This function can be used to get inputs anytime
    inputs:
        @print_msg:msg that should be printed to user
    outputs:
        @input_val:value that user entered
    """

    while True:
        try:
            input_val = int(input(print_msg))
            break
        except ValueError:
            print("Invalid Value")
    return input_val


def main():

    """this is the main function that invokes when the program begin"""

    input_length = get_inputs("Enter list length")

    search_list = sort_list(input_length)
    print(search_list)

    search_num = get_inputs("Enter a Number to search in the list")

    ret_value = binary_search_algo(search_list, search_num)

    if ret_value:
        print("Number is Found")
    else:
        print("Number is not Found")


if __name__ == "__main__":
    main()
