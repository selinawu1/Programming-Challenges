import unittest

from windchill import *


class MyFirstTests(unittest.TestCase):

    def test_windchill(self):
        self.assertEqual(windchill(10.0, 15), -6.5895344209562525)
        self.assertEqual(windchill(0, 25), -24.093780999553864)
        self.assertEqual(windchill(-10, 35), -41.16894662953316)

    def test_temp_index(self):
        self.assertEqual(temp_index(10.0, 15), "Temperature of 10.0 and speed of 15 gives windchill of: -6.5895344209562525")

if __name__ == '__main__':
    unittest.main()
