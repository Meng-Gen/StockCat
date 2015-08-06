#-*- coding: utf-8 -*-

from stockcat.common.string_utils import StringUtils

import datetime
import unittest

class StringUtilsTest(unittest.TestCase):
    def setUp(self):
        self.string_utils = StringUtils()

    def tearDown(self):
        self.string_utils = None

    def test_normalize_number(self):
        actual = self.string_utils.normalize_number('33,825,315')
        expected = 33825315
        self.assertEqual(actual, expected)

        actual = self.string_utils.normalize_number('0')
        expected = 0
        self.assertEqual(actual, expected)

        actual = self.string_utils.normalize_number('-115,859,592')
        expected = -115859592
        self.assertEqual(actual, expected)

        actual = self.string_utils.normalize_number('(27,540)')
        expected = -27540
        self.assertEqual(actual, expected)

        actual = self.string_utils.normalize_number('2.85')
        expected = 2.85
        self.assertEqual(actual, expected)

    def test_from_local_string_to_date(self):
        actual = self.string_utils.from_local_string_to_date(u'2013年12月31日')
        expected = datetime.date(2013, 12, 31)
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_local_string_to_date(u'2012年01月01日')
        expected = datetime.date(2012, 1, 1)
        self.assertEqual(actual, expected)
        
        actual = self.string_utils.from_local_string_to_date('1962/02/09')
        expected = datetime.date(1962, 2, 9)
        self.assertEqual(actual, expected)

    def test_from_local_string_to_date_interval(self):
        actual = self.string_utils.from_local_string_to_date_interval(u'2013年01月01日至2013年12月31日')
        expected = datetime.date(2013, 1, 1), datetime.date(2013, 12, 31)
        self.assertEqual(actual, expected)
        
    def test_from_date_to_roc_era_string(self):
        actual = self.string_utils.from_date_to_roc_era_string(datetime.date(2001, 1, 1))
        expected = '90'
        self.assertEqual(actual, expected)

    def test_from_date_to_2_digit_month_string(self):
        actual = self.string_utils.from_date_to_2_digit_month_string(datetime.date(2001, 1, 1))
        expected = '01'
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_date_to_2_digit_month_string(datetime.date(2001, 10, 31))
        expected = '10'
        self.assertEqual(actual, expected)
