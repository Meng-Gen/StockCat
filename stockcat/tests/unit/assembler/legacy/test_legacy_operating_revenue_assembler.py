#-*- coding: utf-8 -*-

from stockcat.assembler.legacy.legacy_operating_revenue_assembler import LegacyOperatingRevenueAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class LegacyOperatingRevenueAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = LegacyOperatingRevenueAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None

    def test_assemble_2330(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st10?encodeURIComponent=1&run=Y&step=0&colorchg=&TYPEK=sii%20&co_id=2330&off=1&year=99&month=09&firstin=true
        content = self.file_utils.read_file('./stockcat/tests/unit/data/legacy_operating_revenue/2330/2010/09.html')
        column_name_list, row_list = self.assembler.assemble(content)
        self.assertEqual(column_name_list, [u'項目', u'合併營業收入淨額'])
        self.assertEqual(row_list[0], [u'本月', 37637898])
        self.assertEqual(row_list[1], [u'去年同期', 28936225])
        self.assertEqual(row_list[2], [u'增減金額', 8701673])
        self.assertEqual(row_list[3], [u'增減百分比', 30.07])
        self.assertEqual(row_list[4], [u'本年累計', 309395679])
        self.assertEqual(row_list[5], [u'去年累計', 203647791])
        self.assertEqual(row_list[6], [u'增減金額', 105747888])
        self.assertEqual(row_list[7], [u'增減百分比', 51.93])

    def test_assemble_1101(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st10?encodeURIComponent=1&run=Y&step=0&colorchg=&TYPEK=sii%20&co_id=1101&off=1&year=99&month=09&firstin=true
        content = self.file_utils.read_file('./stockcat/tests/unit/data/legacy_operating_revenue/1101/2010/09.html')
        
        # check special case '未公告合併營業收入(採自願公告制)'
        column_name_list, row_list = self.assembler.assemble(content)
        self.assertEqual(column_name_list, [u'未公告合併營業收入(採自願公告制)'])
        self.assertEqual(row_list, [])
