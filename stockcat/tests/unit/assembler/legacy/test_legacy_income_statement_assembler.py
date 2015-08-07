#-*- coding: utf-8 -*-

from stockcat.assembler.legacy.legacy_income_statement_assembler import LegacyIncomeStatementAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class LegacyIncomeStatementAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = LegacyIncomeStatementAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None

    def test_assemble_2330(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st34?encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=false&co_id=2330&year=99&season=03
        content = self.file_utils.read_file('./stockcat/tests/unit/data/legacy_income_statement/2330/2010/03.html')
        column_name_list, row_list = self.assembler.assemble(content)
        
        self.assertEqual(column_name_list, [u'會計科目', datetime.date(2010, 9, 30), datetime.date(2009, 9, 30)])
        self.assertEqual(row_list[0], [(u'銷貨收入總額', 10), 318388370, 102.90, 213468240, 104.82])
        self.assertEqual(row_list[1], [(u'銷貨退回', 10), 8992668, 2.9, 9820449, 4.82])
        self.assertEqual(row_list[2], [(u'銷貨收入淨額', 10), 309395702, 100.00, 203647791, 100.00])
        self.assertEqual(row_list[3], [(u'營業收入合計', 10), 309395702, 100.00, 203647791, 100.00])
        self.assertEqual(row_list[4], [(u'銷貨成本', 10), 157159327, 50.79, 119013880, 58.44])
        self.assertEqual(row_list[5], [(u'營業成本合計', 10), 157159327, 50.79, 119013880, 58.44])
        
        self.assertEqual(row_list[11], [(u'營業淨利(淨損)', 10), 117661857, 38.02, 58320012, 28.63])
        self.assertEqual(row_list[12], [(u'營業外收入及利益', 8)])

        self.assertEqual(row_list[-5], [(u'合併總損益', 10), 121415006, 39.24, 56605811, 27.79])
        self.assertEqual(row_list[-4], [(u'基本每股盈餘', 8)])
        self.assertEqual(row_list[-3], [(u'基本每股盈餘', 10), 4.67, 0.00, 2.19, 0.00])
        self.assertEqual(row_list[-2], [(u'稀釋每股盈餘', 8)])
        self.assertEqual(row_list[-1], [(u'稀釋每股盈餘', 10), 4.66, 0.00, 2.18, 0.00])
