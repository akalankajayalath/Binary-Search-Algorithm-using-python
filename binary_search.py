"""
#module docstring
This program accepts a list from user and search for a given number
uses binary search algorithm.
Functions:
    binary_search(list_to_find_the_number,Number)
"""

import random
import time

def sort_list(length):
    """
    inputs:
        @length:

    outputs:

    Exceptions:
   
    #function docstring
    creating the list as per the users required length
    """
    
    START_TIME = time.time()
    generate_list = []
    for _ in range(length):
        generate_list.append(random.randint(0, 100000))

    generate_list.sort()
    print("--- %s seconds ---" % (time.time() - START_TIME))
    return generate_list




def binary_search_algo(s_list, s_number):

    """
    #function docstring
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


def main():

    """this is the main function that invokes when the program begin"""

    parsed_num2 = False
    while not parsed_num2:
        try:
            input_length = int(input("Enter list length"))
            parsed_num2 = True
        except ValueError:
            print("Invalid Value")

    search_list = sort_list(input_length)
    #print(search_list)

    parsed_num1 = False
    while not parsed_num1:
        try:
            search_num = int(input("Enter a Number to Search"))
            parsed_num1 = True
        except ValueError:
            print("Invalid Value")

    ret_value = binary_search_algo(search_list, search_num)
    if ret_value:
        print("Number is Found")
    else:
        print("Number is not Found")


if __name__ == "__main__":
    main()
