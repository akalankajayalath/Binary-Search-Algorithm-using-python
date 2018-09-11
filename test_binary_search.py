import unittest

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
            #break
        else:
            if s_number < s_list[mid_value]:
                last = mid_value - 1
            else:
                first = mid_value + 1

    return num_found
    
class SimpleTest(unittest.TestCase):
    def testbasic1(self):
        self.assertEqual(binary_search_algo([],2),False) #no value list
        self.assertEqual(binary_search_algo([1,2,5],3),False)#value not in the list
        self.assertEqual(binary_search_algo([1,2,5,4,3],1),True)#1st value of the list
        self.assertEqual(binary_search_algo([1,2,5,4,3],3),True)#last value of the list
        self.assertEqual(binary_search_algo([1,2,5,4,3],5),True)#middle value

    def testExceptions(self):
        self.assertRaises(TypeError,binary_search_algo([1,2,5],'b'))
        self.assertRaises(TypeError,binary_search_algo([1,'b',5],10))

if __name__ == '__main__':
   unittest.main()
