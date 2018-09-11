#module docstring
"""
This program accepts a list from user and search for a given number
uses binary search algorithm.
Functions:
    binary_search(list_to_find_the_number,Number)
"""

import random
import time

START_TIME = time.time()

def sort_list(length):

    #function docstring
    """creating the list as per the users required length"""
    generate_list = []
    for j in range(length):
        generate_list.append(random.randint(0, 100000))
    #generate_list = random.sample(range(100000), length)
    generate_list.sort()
    return generate_list

def binary_search_algo(s_list, s_number):

    #function docstring
    """search for the given number in a list
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

print("--- %s seconds ---" % (time.time() - START_TIME))

def main():
    """this is the main function that invokes when the program begin"""
    input_length = int(input("Enter list length"))
    search_list = sort_list(input_length)
    print(search_list)

    parsed_num = False
    while not parsed_num:
        try:
            search_num = int(input("Enter a Number to Search"))
            parsed_num = True
        except ValueError:
            print("Invalid Value")

    ret_value = binary_search_algo(search_list, search_num)
    if ret_value:
        print("Number is Found")
    else:
        print("Number is not Found")

if __name__ == "__main__":
    main()
