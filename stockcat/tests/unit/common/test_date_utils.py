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
        