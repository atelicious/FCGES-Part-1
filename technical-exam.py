#FCGES Technical Exam Part 1
import unittest


""" 1. Given an array A of N integers, write a function ​missing_int(A) that returns the smallest positive integer 
(greater than 0) that does not occur in A.
○ A = [1, 3, 6, 4, 1, 2] should return 5 
○ A = [1, 2, 3] should return 4 
○ A = [-1, -1, -1, -5] should return 1 
○ A = [1, 3, 6, 4, 1, 7, 8, 10] should return 2"""

"""2. Write a ​rotate(A, k)
​ function which returns a rotated array A, k times; that is, each element of A will be shifted to the right k times 
○ rotate([3, 8, 9, 7, 6], 3) returns [9, 7, 6, 3, 8] 
○ rotate([0, 0, 0], 1) returns [0, 0, 0] 
○ rotate([1, 2, 3, 4], 4) returns [1, 2, 3, 4] """


def missing_int(A):
    min_value = min(A)
    max_value = max(A)

    if max_value <= 0:
        return 1

    d = {i:0 for i in range(min_value, max_value+1)}

    for items in A:
        if items in d:
            d[items] += 1
    
    for items in d:
        if d[items] == 0 and items > 0:
            return(items)
        
    return(max_value + 1)

    

def rotate(A, K):
    while K > 0:
        last = A.pop(len(A)-1)
        A.insert(0, last)
        K -=1

    return A

a = missing_int([1, 3, 6, 4, 1, 2])


#================================================
#Unit tests
class MissingIntTest(unittest.TestCase):

    def test_missing_int1(self):
        self.assertEqual(missing_int([1, 3, 6, 4, 1, 2]), 5)
    def test_missing_int2(self):
        self.assertEqual(missing_int([1, 2, 3]), 4)
    def test_missing_int3(self):
        self.assertEqual(missing_int([-1, -1, -1, -5] ), 1)
    def test_missing_int4(self):
        self.assertEqual(missing_int([1, 3, 6, 4, 1, 7, 8, 10]), 2)

class RotateTest(unittest.TestCase):

    def test_rotate1(self):
        self.assertEqual(rotate([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
    def test_rotate2(self):
        self.assertEqual(rotate([0, 0, 0], 1), [0, 0, 0])
    def test_rotate3(self):
        self.assertEqual(rotate([1, 2, 3, 4], 4), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()