
import unittest #import the unittest module
from app.calculator import Calculator   #import the calculator module from the app package

class TestCalculator(unittest.TestCase):
    #---Test cases for the Calculator class---
    
    def setUp(self):
        #Set up a Calculator instance for each test
        self.calc = Calculator()
    
    def test_add(self):
        #Test addition with positive and negative numbers
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_subtract(self):
        #Test subtraction with differnt numbers
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(-5, -10), 5)
    
    def test_multiply(self):
        #Test multiplication with different numbers
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-2, -5), 10)
    
    def test_divide(self):
        #Test the division with different numbers
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(12, 3), 4)
    
    def test_divide_by_zero(self):
        #Test division when dividing by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()

