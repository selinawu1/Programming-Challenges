import unittest

from the_99_trick import *


class MyFirstTests(unittest.TestCase):

    def test_yourPart(self):
        self.assertEqual(your_Part(15), 84)

    def test_friendsPart(self):
        self.assertEqual(friends_Part(84), "I said the answer was 15 and the calculation result is 15")
        
    
if __name__ == '__main__':
    unittest.main()
