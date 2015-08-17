#-*- coding: utf-8 -*-

from stockcat.assembler.assemble_error import NoRecordAssembleError
from stockcat.assembler.operating_revenue_summary_assembler import OperatingRevenueSummaryAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class OperatingRevenueSummaryAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = OperatingRevenueSummaryAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None
    
    def test_assemble_stock_exchange_market_in_2010(self):
        # online: http://mops.twse.com.tw/nas/t21/sii/t21sc03_99_9.html
        content = self.file_utils.read_file('./stockcat/tests/unit/data/operating_revenue_summary/stock_exchange_market/2010/9.html')
        dao = self.assembler.assemble(content, datetime.date(2010, 9, 30))

        actual = dao.get_column_name_list()
        expected = [u'公司代號', u'公司名稱', u'當月營收', u'上月營收', u'去年當月營收', u'上月比較增減(%)', u'去年同月增減(%)', u'當月累計營收', u'去年累計營收', u'前期比較增減(%)']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'1101', u'台泥', 1804805, 1861703, 1823433, -3.05, -1.02, 16344206, 15719543, 3.97])
        for row in row_list:
            self.assertEqual(len(row), 10)

        self.assertEqual(dao.get_stmt_date(), datetime.date(2010, 9, 30))
        self.assertEqual(dao.get_release_date(), datetime.date(2013, 5, 7))

    def test_assemble_stock_exchange_market_in_2012(self):
        # online: http://mops.twse.com.tw/nas/t21/sii/t21sc03_101_1.html
        content = self.file_utils.read_file('./stockcat/tests/unit/data/operating_revenue_summary/stock_exchange_market/2012/1.html')
        dao = self.assembler.assemble(content, datetime.date(2012, 1, 31))

        actual = dao.get_column_name_list()
        expected = [u'公司代號', u'公司名稱', u'當月營收', u'上月營收', u'去年當月營收', u'上月比較增減(%)', u'去年同月增減(%)', u'當月累計營收', u'去年累計營收', u'前期比較增減(%)']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'1101', u'台泥', 1752202, 2072570, 2337946, -15.45, -25.05, 1752202, 2337946, -25.05])
        self.assertEqual(row_list[7], [u'1201', u'味全公司', 1115106, 1127058, 1110017, -1.06, 0.45, 1115106, 1110017, 0.45])
        self.assertEqual(row_list[-1], [u'912398', u'友佳國際', 420469, 576524, 742870, -27.06, -43.39, 420469, 742870, -43.39])
        for row in row_list:
            self.assertEqual(len(row), 10)

        self.assertEqual(dao.get_stmt_date(), datetime.date(2012, 1, 31))
        self.assertEqual(dao.get_release_date(), datetime.date(2015, 6, 25))

    def test_assemble_stock_exchange_market_in_February_2013(self):
        # online: http://mops.twse.com.tw/nas/t21/sii/t21sc03_102_2.html
        content = self.file_utils.read_file('./stockcat/tests/unit/data/operating_revenue_summary/stock_exchange_market/2013/2.html')
        dao = self.assembler.assemble(content, datetime.date(2013, 2, 28))

        actual = dao.get_column_name_list()
        expected = [u'公司代號', u'公司名稱', u'當月營收', u'上月營收', u'去年當月營收', u'上月比較增減(%)', u'去年同月增減(%)', u'當月累計營收', u'去年累計營收', u'前期比較增減(%)']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'1101', u'台泥', 5540346, 9134465, 7983023, -39.34, -30.59, 14674811, 15108059, -2.86])
        self.assertEqual(row_list[-1], [u'912398', u'友佳國際', 245279, 547037, 701056, -55.16, -65.01, 792316, 1121522, -29.35])
        for row in row_list:
            self.assertEqual(len(row), 10)

        self.assertEqual(dao.get_stmt_date(), datetime.date(2013, 2, 28))
        self.assertEqual(dao.get_release_date(), datetime.date(2015, 6, 25))

    def test_assemble_stock_exchange_market_in_2014(self):
        # online: http://mops.twse.com.tw/nas/t21/sii/t21sc03_103_1.html
        content = self.file_utils.read_file('./stockcat/tests/unit/data/operating_revenue_summary/stock_exchange_market/2014/1.html')
        dao = self.assembler.assemble(content, datetime.date(2014, 1, 31))

        actual = dao.get_column_name_list()
        expected = [u'公司代號', u'公司名稱', u'當月營收', u'上月營收', u'去年當月營收', u'上月比較增減(%)', u'去年同月增減(%)', u'當月累計營收', u'去年累計營收', u'前期比較增減(%)']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'1101', u'台泥', 9801691, 11416657, 9134465, -14.14, 7.30, 9801691, 9134465, 7.30])
        for row in row_list:
            self.assertEqual(len(row), 10)

        self.assertEqual(dao.get_stmt_date(), datetime.date(2014, 1, 31))
        self.assertEqual(dao.get_release_date(), datetime.date(2015, 2, 1))

    def test_assemble_stock_exchange_market_in_2015(self):
        # online: http://mops.twse.com.tw/nas/t21/sii/t21sc03_104_1.html
        content = self.file_utils.read_file('./stockcat/tests/unit/data/operating_revenue_summary/stock_exchange_market/2015/1.html')
        dao = self.assembler.assemble(content, datetime.date(2015, 1, 31))

        actual = dao.get_column_name_list()
        expected = [u'公司代號', u'公司名稱', u'當月營收', u'上月營收', u'去年當月營收', u'上月比較增減(%)', u'去年同月增減(%)', u'當月累計營收', u'去年累計營收', u'前期比較增減(%)']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'1101', u'台泥', 8921719, 9913147, 9801691, -10.00, -8.97, 8921719, 9801691, -8.97])
        for row in row_list:
            self.assertEqual(len(row), 10)

        self.assertEqual(dao.get_stmt_date(), datetime.date(2015, 1, 31))
        self.assertEqual(dao.get_release_date(), datetime.date(2015, 8, 16))

    def test_assemble_otc_market_in_2010(self):
        # online: http://mops.twse.com.tw/nas/t21/otc/t21sc03_99_9.html
        content = self.file_utils.read_file('./stockcat/tests/unit/data/operating_revenue_summary/otc_market/2010/9.html')
        dao = self.assembler.assemble(content, datetime.date(2010, 9, 30))

        actual = dao.get_column_name_list()
        expected = [u'公司代號', u'公司名稱', u'當月營收', u'上月營收', u'去年當月營收', u'上月比較增減(%)', u'去年同月增減(%)', u'當月累計營收', u'去年累計營收', u'前期比較增減(%)']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'4205', u'恆義公司', 92492, 112118, 92552, -17.50, -0.06, 871040, 840174, 3.67])
        for row in row_list:
            self.assertEqual(len(row), 10)

        self.assertEqual(dao.get_stmt_date(), datetime.date(2010, 9, 30))
        self.assertEqual(dao.get_release_date(), datetime.date(2013, 5, 7))

    def test_assemble_otc_market_in_2014(self):
        # online: http://mops.twse.com.tw/nas/t21/otc/t21sc03_103_9.html
        content = self.file_utils.read_file('./stockcat/tests/unit/data/operating_revenue_summary/otc_market/2014/9.html')
        dao = self.assembler.assemble(content, datetime.date(2014, 9, 30))

        actual = dao.get_column_name_list()
        expected = [u'公司代號', u'公司名稱', u'當月營收', u'上月營收', u'去年當月營收', u'上月比較增減(%)', u'去年同月增減(%)', u'當月累計營收', u'去年累計營收', u'前期比較增減(%)']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'1256', u'F-鮮活', 193070, 208084, 181554, -7.21, 6.34, 1660110, 1368966, 21.26])
        for row in row_list:
            self.assertEqual(len(row), 10)

        self.assertEqual(dao.get_stmt_date(), datetime.date(2014, 9, 30))
        self.assertEqual(dao.get_release_date(), datetime.date(2015, 8, 16))

    def test_assemble_otc_market_in_2015(self):
        # online: http://mops.twse.com.tw/nas/t21/otc/t21sc03_104_1.html
        content = self.file_utils.read_file('./stockcat/tests/unit/data/operating_revenue_summary/otc_market/2015/1.html')
        dao = self.assembler.assemble(content, datetime.date(2015, 1, 31))

        actual = dao.get_column_name_list()
        expected = [u'公司代號', u'公司名稱', u'當月營收', u'上月營收', u'去年當月營收', u'上月比較增減(%)', u'去年同月增減(%)', u'當月累計營收', u'去年累計營收', u'前期比較增減(%)']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'1256', u'F-鮮活', 209686, 148468, 154455, 41.23, 35.75, 209686, 154455, 35.75])
        for row in row_list:
            self.assertEqual(len(row), 10)

        self.assertEqual(dao.get_stmt_date(), datetime.date(2015, 1, 31))
        self.assertEqual(dao.get_release_date(), datetime.date(2015, 8, 16))

    def test_assemble_raise_no_record_assemble_error(self):
        # online: http://mops.twse.com.tw/nas/t21/sii/t21sc03_105_1.html
        content = self.file_utils.read_file('./stockcat/tests/unit/data/error/url_not_found_error.html')
        with self.assertRaises(NoRecordAssembleError) as context:
            self.assembler.assemble(content, datetime.date(2016, 1, 31))
        self.assertEqual(context.exception.param['date'], datetime.date(2016, 1, 31))   
