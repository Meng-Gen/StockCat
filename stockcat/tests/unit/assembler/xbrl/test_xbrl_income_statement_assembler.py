#-*- coding: utf-8 -*-

from stockcat.assembler.xbrl.xbrl_income_statement_assembler import XbrlIncomeStatementAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class XbrlIncomeStatementAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = XbrlIncomeStatementAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None

    def test_assemble_2330(self):
        # online: http://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID=2330&SYEAR=2014&SSEASON=3&REPORT_ID=C
        content = self.file_utils.read_file('./stockcat/tests/unit/data/xbrl_financial_statement/2330/2014/03.html')
        column_name_list, row_list = self.assembler.assemble(content)
        self.assertEqual(column_name_list[0], u'會計項目')
        self.assertEqual(column_name_list[1], (datetime.date(2014, 1, 1), datetime.date(2014, 9, 30)))
        self.assertEqual(column_name_list[2], (datetime.date(2013, 1, 1), datetime.date(2013, 9, 30)))
        self.assertEqual(row_list[0], [(u'營業收入', 2)])
        self.assertEqual(row_list[1], [(u'營業收入合計', 3), 209049734, 162577034, 540285390, 451218350])
    