import unittest
from pathlib import Path

from league_table_10 import *


class testingLeagueTable(unittest.TestCase):

    def test_check_file_exists(self):
        csv_file = Path("test.csv")
        self.assertIsNotNone(check_file_exists(csv_file))
        self.assertFalse(check_file_exists(csv_file))

        csv_file = Path("Premier 16-17.csv")
        self.assertTrue(check_file_exists(csv_file))

        csv_file = Path("blank.csv")
        self.assertTrue(check_file_exists(csv_file))

        csv_file = Path("one_row.csv")
        self.assertTrue(check_file_exists(csv_file))

    def test_read_csv(self):
        csv_file = Path("test.csv")
        self.assertListEqual([], read_csv(csv_file))

        csv_file = Path("Premier 16-17.csv")
        self.assertGreaterEqual(len(read_csv(csv_file)), 1)

        csv_file = Path("blank.csv")
        self.assertListEqual([], read_csv(csv_file))

        csv_file = Path("one_row.csv")
        self.assertListEqual([["test", '10']], read_csv(csv_file))

    def test_process_results(self):
        csv_file = Path("test.csv")
        self.assertEqual(process_results(read_csv(csv_file)).get("Chelsea"), [30, 3, 5, 52, 93])

    def test_mostleast_accurate(self):
        csv_file = Path("Premier 16-17.csv")
        self.assertEqual(mostleast_accurate(read_csv(csv_file)), ["Tottenham", "Middlesbrough"])

    def test_dirtiest(self):
        csv_file = Path("Premier 16-17.csv")
        self.assertEqual(dirtiest(read_csv(csv_file)), ["Crystal Palace", "Burnley"])

    def test_card_average(self):
        csv_file = Path("Premier 16-17.csv")
        self.assertEqual(card_average(read_csv(csv_file)), ["R Madley", "C Kavanagh"])
      

if __name__ == '__main__':
    unittest.main()
