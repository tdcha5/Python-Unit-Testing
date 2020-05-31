import unittest
import calc 
import HtmlTestRunner

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.calculate("Add",10,5), 15)
        
        ## Edge cases for add functions
        self.assertEqual(calc.calculate("Add",-1, 1), -0)
        self.assertEqual(calc.calculate("Add",-1, -1), -2)
        
    def test_subtract(self):
        self.assertEqual(calc.calculate("Subtract",10,5), 5)
        self.assertEqual(calc.calculate("Subtract",-1,1), -2)
        self.assertEqual(calc.calculate("Subtract",-1,-1), 0)
        
    def test_multiply(self):
        self.assertEqual(calc.calculate("Multiply",10,5),50)
        self.assertEqual(calc.calculate("Multiply",-1,1), -1)
        self.assertEqual(calc.calculate("Multiply",-1,-1), 1)
        
    def test_divide(self):
        self.assertEqual(calc.calculate("Divide",10,5), 2)
        self.assertEqual(calc.calculate("Divide",-1,1), -1)
        self.assertEqual(calc.calculate("Divide",5,2), 2.5)
        
        
if __name__ == '__main__':
    ##unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/torid/Documents/projects/calc_test/reports'))