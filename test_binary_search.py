import unittest
from binary_search import binary_search_algo 

class SimpleTest(unittest.TestCase):
    def testbasic1(self):
        self.assertEqual(binary_search_algo([],2),False) #no value list
        self.assertEqual(binary_search_algo([1,2,5],3),False)#value not in the list
        self.assertEqual(binary_search_algo([1,2,3,4,5],1),True)#1st value of the list
        self.assertEqual(binary_search_algo([1,2,3,4,5],3),True)#last value of the list
        self.assertEqual(binary_search_algo([1,2,3,4,5],5),True)#middle value

    def testExceptions(self):
        self.assertRaises(TypeError,binary_search_algo([1,2,5],'b'))
        self.assertRaises(TypeError,binary_search_algo([1,'b',5],10))

if __name__ == '__main__':
   unittest.main()
