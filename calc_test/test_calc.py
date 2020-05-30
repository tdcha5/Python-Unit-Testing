import unittest
import calc 

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)
        
      ### Add a test case for each operator so that I can run it as I make changes to calc.py
        
if __name__ == '__main__':
    unittest.main()