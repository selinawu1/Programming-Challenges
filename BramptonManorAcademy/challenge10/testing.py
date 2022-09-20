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

    def test_mostleast_accurate(self):
        rows = [["13/08/2016", "Burnley", "Swansea", 0, 1,"A", "J Moss", 10, 17, 3, 9, 10, 14, 7, 4, 3, 2, 0, 0],
                ["13/08/2016", "Crystal Palace", "West Brom", 0, 1, "A", "C Pawson", 14, 13, 4, 3, 12, 15, 3, 6, 2, 2, 0, 0]]
        self.assertEqual(mostleast_accurate(rows), ["Swansea", "Burnley"])

    def test_dirtiest(self):
        rows = [["13/08/2016", "Burnley", "Swansea", 0, 1, "A", "J Moss", 10, 17, 3, 9, 10, 14, 7, 4, 3, 2, 0, 0],
                ["13/08/2016", "Crystal Palace", "West Brom", 0, 1, "A", "C Pawson", 14, 13, 4, 3, 12, 15, 3, 6, 2, 2, 0,
                 0]]
        self.assertEqual(dirtiest(rows), ["West Brom", "Burnley"])

    def test_card_average(self):
        rows = [["13/08/2016", "Burnley", "Swansea", 0, 1,"A", "J Moss", 10, 17, 3, 9, 10, 14, 7, 4, 3, 2, 0, 0],
                ["13/08/2016", "Crystal Palace" ,"West Brom", 0, 1, "A", "C Pawson", 14, 13, 4, 3, 12, 15, 3, 6, 2, 2, 0, 0]]
        self.assertEqual(card_average(rows), ["J Moss", "C Pawson"])

    def test_process_results(self):
        rows = [["13/08/2016","Burnley","Swansea",0,1,"A","J Moss",10,17,3,9,10,14,7,4,3,2,0,0]]
        output = {"Burnley": [0, 0, 1, -1, 0], "Swansea":[1, 0, 0, 1, 3]}
        self.assertEqual(process_results(rows), output)

if __name__ == '__main__':
    unittest.main()
