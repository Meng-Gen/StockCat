#-*- coding: utf-8 -*-

from stockcat.common.date_utils import DateUtils

import datetime
import unittest

class DateUtilsTest(unittest.TestCase):
    def setUp(self):
        self.date_utils = DateUtils()

    def tearDown(self):
        self.date_utils = None

    def test_get_last_date_of_month(self):
        actual = self.date_utils.get_last_date_of_month(datetime.date(2010, 1, 1))
        expected = datetime.date(2010, 1, 31)
        self.assertEqual(actual, expected)

    def test_get_last_date_of_prev_month(self):
        actual = self.date_utils.get_last_date_of_prev_month(datetime.date(2010, 1, 1))
        expected = datetime.date(2009, 12, 31)
        self.assertEqual(actual, expected)

    def test_get_last_date_of_quarter(self):
        actual = self.date_utils.get_last_date_of_quarter(datetime.date(2010, 1, 1))
        expected = datetime.date(2010, 3, 31)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_quarter(datetime.date(2010, 3, 31))
        expected = datetime.date(2010, 3, 31)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_quarter(datetime.date(2010, 4, 1))
        expected = datetime.date(2010, 6, 30)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_quarter(datetime.date(2010, 6, 30))
        expected = datetime.date(2010, 6, 30)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_quarter(datetime.date(2010, 7, 1))
        expected = datetime.date(2010, 9, 30)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_quarter(datetime.date(2010, 9, 30))
        expected = datetime.date(2010, 9, 30)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_quarter(datetime.date(2010, 10, 1))
        expected = datetime.date(2010, 12, 31)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_quarter(datetime.date(2010, 12, 31))
        expected = datetime.date(2010, 12, 31)
        self.assertEqual(actual, expected)

    def test_get_last_date_of_next_quarter(self):
        actual = self.date_utils.get_last_date_of_next_quarter(datetime.date(2010, 1, 1))
        expected = datetime.date(2010, 6, 30)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_next_quarter(datetime.date(2010, 3, 31))
        expected = datetime.date(2010, 6, 30)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_next_quarter(datetime.date(2010, 4, 1))
        expected = datetime.date(2010, 9, 30)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_next_quarter(datetime.date(2010, 6, 30))
        expected = datetime.date(2010, 9, 30)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_next_quarter(datetime.date(2010, 7, 1))
        expected = datetime.date(2010, 12, 31)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_next_quarter(datetime.date(2010, 9, 30))
        expected = datetime.date(2010, 12, 31)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_next_quarter(datetime.date(2010, 10, 1))
        expected = datetime.date(2011, 3, 31)
        self.assertEqual(actual, expected)

        actual = self.date_utils.get_last_date_of_next_quarter(datetime.date(2010, 12, 31))
        expected = datetime.date(2011, 3, 31)
        self.assertEqual(actual, expected)

    def test_range_date_by_month(self):
        actual = self.date_utils.range_date_by_month(datetime.date(2010, 9, 1), datetime.date(2011, 3, 15))
        expected = [
                datetime.date(2010, 9, 30), 
                datetime.date(2010, 10, 31), 
                datetime.date(2010, 11, 30), 
                datetime.date(2010, 12, 31), 
                datetime.date(2011, 1, 31), 
                datetime.date(2011, 2, 28), 
                datetime.date(2011, 3, 31), 
        ]
        self.assertEqual(actual, expected)

    def test_range_date_by_quarter(self):
        actual = self.date_utils.range_date_by_quarter(datetime.date(2010, 9, 1), datetime.date(2011, 3, 15))
        expected = [
                datetime.date(2010, 9, 30), 
                datetime.date(2010, 12, 31), 
                datetime.date(2011, 3, 31), 
        ]
        self.assertEqual(actual, expected)
