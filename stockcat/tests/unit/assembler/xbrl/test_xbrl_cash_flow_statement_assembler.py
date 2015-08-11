#-*- coding: utf-8 -*-

from stockcat.assembler.xbrl.xbrl_cash_flow_statement_assembler import XbrlCashFlowStatementAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class XbrlCashFlowStatementAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = XbrlCashFlowStatementAssembler()
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
        self.assertEqual(row_list[0], [(u'營業活動之現金流量－間接法', 2)])
