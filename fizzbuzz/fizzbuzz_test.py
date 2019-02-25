import unittest
from fizzbuzz import fizzbuzz

class FizzbuzTest(unittest.TestCase):
    def test_test1(self):
        self.assertEqual(fizzbuzz([1, 2, 3], [ ]) ,'fizz')
    def test_test2(self):
        self.assertEqual(fizzbuzz([1, 2, 3], [1, 2]) ,'buzz')
    def test_test3(self):
        self.assertEqual(fizzbuzz([1, 2, 3], [1]) ,4)
    def test_emptylist(self):
        self.assertEqual(fizzbuzz([1, 2, 3], (1)) ,'one of the entries is not a list')
        
if __name__ == '__main__':
    unittest.main()
