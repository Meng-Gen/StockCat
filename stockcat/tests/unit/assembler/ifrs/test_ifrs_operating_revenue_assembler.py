#-*- coding: utf-8 -*-

from stockcat.assembler.ifrs.ifrs_operating_revenue_assembler import IfrsOperatingRevenueAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class IfrsOperatingRevenueAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = IfrsOperatingRevenueAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None

    def test_assemble_2330(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st10_ifrs?encodeURIComponent=1&run=Y&step=0&colorchg=&TYPEK=sii%20&co_id=2330&off=1&year=103&month=09&firstin=true
        content = self.file_utils.read_file('./stockcat/tests/unit/data/ifrs_operating_revenue/2330/2014/09.html')

        dao = self.assembler.assemble(content)
        column_name_list = dao.get_column_name_list()
        row_list = dao.get_row_list()

        self.assertEqual(column_name_list, [u'項目', datetime.date(2014, 9, 30)])
        self.assertEqual(row_list[0], [u'本月', 74846313])
        self.assertEqual(row_list[1], [u'去年同期', 55382473])
        self.assertEqual(row_list[2], [u'增減金額', 19463840])
        self.assertEqual(row_list[3], [u'增減百分比', 35.14])
        self.assertEqual(row_list[4], [u'本年累計', 540285390])
        self.assertEqual(row_list[5], [u'去年累計', 451218350])
        self.assertEqual(row_list[6], [u'增減金額', 89067040])
        self.assertEqual(row_list[7], [u'增減百分比', 19.74])

    def test_assemble_1101(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st10_ifrs?encodeURIComponent=1&run=Y&step=0&colorchg=&TYPEK=sii%20&co_id=1101&off=1&year=103&month=09&firstin=true        
        content = self.file_utils.read_file('./stockcat/tests/unit/data/ifrs_operating_revenue/1101/2014/09.html')

        dao = self.assembler.assemble(content)
        column_name_list = dao.get_column_name_list()
        row_list = dao.get_row_list()

        # check negative number
        self.assertEqual(row_list[2], [u'增減金額', -244950])
        self.assertEqual(row_list[3], [u'增減百分比', -2.43])
        self.assertEqual(row_list[7], [u'增減百分比', 7.00])
