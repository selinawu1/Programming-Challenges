import unittest

from slayer import *


class MyFirstTests(unittest.TestCase):

    def test_layers(self):
        self.assertEqual(layers(666666), 666666)
        self.assertEqual(layers(142857), 428571)

    def test_slayer(self):
        self.assertEqual(slayer(666666), False)
        self.assertEqual(slayer(142857), True)

if __name__ == '__main__':
    unittest.main()
		
