#-*- coding: utf-8 -*-

from stockcat.assembler.operating_revenue_summary_assembler import OperatingRevenueSummaryAssembler
from stockcat.common.file_utils import FileUtils
#from stockcat.dao.operating_revenue_dao import OperatingRevenueDao

import datetime
import unittest

class OperatingRevenueSummaryAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = OperatingRevenueSummaryAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None
    
    def test_assemble_stock_exchange_market(self):
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

    def test_assemble_otc_market(self):
        # online: http://mops.twse.com.tw/nas/t21/otc/t21sc03_104_1.html
        pass
