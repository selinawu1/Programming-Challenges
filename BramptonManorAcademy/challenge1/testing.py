import unittest

from rod_conversions import *


class MyFirstTests(unittest.TestCase):

    def test_rodsIntoMeters(self):
        self.assertEqual(rodsIntoMeters(1), 5.0292)


if __name__ == '__main__':
    unittest.main()
