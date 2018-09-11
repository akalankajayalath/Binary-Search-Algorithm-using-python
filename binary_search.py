#module docstring
"""
This program accepts a list from user and search for a given number
uses binary search algorithm.
Functions:
    binary_search(list_to_find_the_number,Number)
"""

#TO DO
    #pylinting - done
    #perfomance,time complexity
    #pytest: unit-testing
    #random number list - done
    #efficiency of sort function
import random

#S = input("Enter your list(seperate numbers with spaces)")
#SEARCHNUMLIST = list(map(int, S.split())) #splitting numbers and creating list
SEARCHNUMLIST = random.sample(range(100000), 10)
SEARCHNUMLIST.sort()
print(SEARCHNUMLIST)

#search function using binary search algorithm
def binary_search_algo(s_list, s_number):

    #function docstring
    """search for the given number in a list"""

    first = 0
    last = len(s_list) - 1
    num_found = False

    while last >= first and not num_found:
        mid_value = (first + last)//2

        if s_list[mid_value] == s_number:
            num_found = True
            #return True;
            break
        else:
            if s_number < s_list[mid_value]:
                last = mid_value - 1
            else:
                first = mid_value + 1

    return num_found

parsed_num = False
while not parsed:
    try:
        SEARCHNUM = int(input("Enter a Number to Search"))
        parsed_num = True
    except ValueError:
        print("Invalid Value")

RETVALUE = binary_search_algo(SEARCHNUMLIST, SEARCHNUM)

if RETVALUE:
    print("Number is Found")
else:
    print("Number is not Found")
