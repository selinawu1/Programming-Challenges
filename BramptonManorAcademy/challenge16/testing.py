import unittest

from debt_management import *


class MyFirstTests(unittest.TestCase):

    def test_interest(self):
        self.assertEqual(interest(10, 100), 10)
        self.assertEqual(interest(12, 100), 12)
        self.assertEqual(interest(10, 20), 2)

    def test_repayment(self):
        self.assertEqual(repayment(100, 50), 50)
        self.assertEqual(repayment(111, 50), 55.5)


if __name__ == '__main__':
    unittest.main()
