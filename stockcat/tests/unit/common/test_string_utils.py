#-*- coding: utf-8 -*-

from stockcat.common.string_utils import StringUtils

import datetime
import unittest

class StringUtilsTest(unittest.TestCase):
    def setUp(self):
        self.string_utils = StringUtils()

    def tearDown(self):
        self.string_utils = None

    def test_normalize_arabic_number(self):
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

        actual = self.string_utils.normalize_number('170,270,395.00')
        expected = 170270395
        self.assertEqual(actual, expected)

        actual = self.string_utils.normalize_number('(  10,117,111)')
        expected = -10117111
        self.assertEqual(actual, expected)

    def test_normalize_none_number(self):
        actual = self.string_utils.normalize_number(u'-')
        expected = None
        self.assertEqual(actual, expected)

        actual = self.string_utils.normalize_number(u'')
        expected = None
        self.assertEqual(actual, expected)

        actual = self.string_utils.normalize_number(u'不適用')
        expected = None
        self.assertEqual(actual, expected)

    def test_normalize_chinese_number(self):
        actual = self.string_utils.normalize_number(u'九十九')
        expected = 99
        self.assertEqual(actual, expected)

        actual = self.string_utils.normalize_number(u'九十')
        expected = 90
        self.assertEqual(actual, expected)

        actual = self.string_utils.normalize_number(u'三')
        expected = 3
        self.assertEqual(actual, expected)

    def test_normalize_percentage(self):
        actual = self.string_utils.normalize_number(u'20.92%')
        expected = 0.2092
        self.assertAlmostEqual(actual, expected)

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

        actual = self.string_utils.from_local_string_to_date(u'2015/08/13')
        expected = datetime.date(2015, 8, 13)
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_local_string_to_date(u'民國103年09月')
        expected = datetime.date(2014, 9, 30)
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_local_string_to_date(u'104')
        expected = datetime.date(2015, 12, 31)
        self.assertEqual(actual, expected)

    def test_roc_era_from_local_string_to_date(self):
        actual = self.string_utils.from_local_string_to_date(u'99年09月30日')
        expected = datetime.date(2010, 9, 30)
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_local_string_to_date(u'102/05/07')
        expected = datetime.date(2013, 5, 7)
        self.assertEqual(actual, expected)

    def test_from_local_string_to_date_interval(self):
        actual = self.string_utils.from_local_string_to_date_period(u'2013年01月01日至2013年12月31日')
        expected = datetime.date(2013, 1, 1), datetime.date(2013, 12, 31)
        self.assertEqual(actual, expected)

    def test_roc_era_from_local_string_to_date_period(self):
        actual = self.string_utils.from_local_string_to_date_period(u'九十八年前三季')
        expected = datetime.date(2009, 1, 1), datetime.date(2009, 9, 30)
        self.assertEqual(actual, expected)
        
        actual = self.string_utils.from_local_string_to_date_period(u'100年第一季')
        expected = datetime.date(2011, 1, 1), datetime.date(2011, 3, 31)
        self.assertEqual(actual, expected)
        
        actual = self.string_utils.from_local_string_to_date_period(u'100年上半年度')
        expected = datetime.date(2011, 1, 1), datetime.date(2011, 6, 30)
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_local_string_to_date_period(u'99年上半年度')
        expected = datetime.date(2010, 1, 1), datetime.date(2010, 6, 30)
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_local_string_to_date_period(u'100年前三季')
        expected = datetime.date(2011, 1, 1), datetime.date(2011, 9, 30)
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_local_string_to_date_period(u'100年度')
        expected = datetime.date(2011, 1, 1), datetime.date(2011, 12, 31)
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

    def test_from_date_to_2_digit_quarter_string(self):
        # spring
        actual = self.string_utils.from_date_to_2_digit_quarter_string(datetime.date(2001, 1, 1))
        expected = '01'
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_date_to_2_digit_quarter_string(datetime.date(2001, 3, 31))
        expected = '01'
        self.assertEqual(actual, expected)

        # summer
        actual = self.string_utils.from_date_to_2_digit_quarter_string(datetime.date(2001, 4, 1))
        expected = '02'
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_date_to_2_digit_quarter_string(datetime.date(2001, 6, 30))
        expected = '02'
        self.assertEqual(actual, expected)

        # fall
        actual = self.string_utils.from_date_to_2_digit_quarter_string(datetime.date(2001, 7, 1))
        expected = '03'
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_date_to_2_digit_quarter_string(datetime.date(2001, 9, 30))
        expected = '03'
        self.assertEqual(actual, expected)

        # winter
        actual = self.string_utils.from_date_to_2_digit_quarter_string(datetime.date(2001, 10, 1))
        expected = '04'
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_date_to_2_digit_quarter_string(datetime.date(2001, 12, 31))
        expected = '04'
        self.assertEqual(actual, expected)

    def test_from_date_to_1_digit_quarter_string(self):
        # spring
        actual = self.string_utils.from_date_to_1_digit_quarter_string(datetime.date(2001, 1, 1))
        expected = '1'
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_date_to_1_digit_quarter_string(datetime.date(2001, 3, 31))
        expected = '1'
        self.assertEqual(actual, expected)

        # summer
        actual = self.string_utils.from_date_to_1_digit_quarter_string(datetime.date(2001, 4, 1))
        expected = '2'
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_date_to_1_digit_quarter_string(datetime.date(2001, 6, 30))
        expected = '2'
        self.assertEqual(actual, expected)

        # fall
        actual = self.string_utils.from_date_to_1_digit_quarter_string(datetime.date(2001, 7, 1))
        expected = '3'
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_date_to_1_digit_quarter_string(datetime.date(2001, 9, 30))
        expected = '3'
        self.assertEqual(actual, expected)

        # winter
        actual = self.string_utils.from_date_to_1_digit_quarter_string(datetime.date(2001, 10, 1))
        expected = '4'
        self.assertEqual(actual, expected)

        actual = self.string_utils.from_date_to_1_digit_quarter_string(datetime.date(2001, 12, 31))
        expected = '4'
        self.assertEqual(actual, expected)

    def test_is_match_seperation(self):
        pattern = u'^(-| |=)*$'
        self.assertTrue(self.string_utils.is_match(pattern, u'======      ======'))
        self.assertTrue(self.string_utils.is_match(pattern, u'------      ------'))
        self.assertFalse(self.string_utils.is_match(pattern, u'同時影響現金及非現金項目之投資活動：'))

    def test_match_account(self):
        pattern = u'^([^\s]*)：$'
        actual = self.string_utils.match(pattern, u'營業活動之現金流量：')
        expected = [u'營業活動之現金流量']
        self.assertEqual(actual, expected)
