import unittest
from Fizzbuzz import fizzbuzz
class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz")  
        
        self.assertEqual(fizzbuzz(9), "fizz")      
        
        self.assertEqual(fizzbuzz(10), "buzz")     
       
        self.assertEqual(fizzbuzz(7), "The number is not a multiple of 3 or 5.")  

if __name__ == "__main__":
    unittest.main()