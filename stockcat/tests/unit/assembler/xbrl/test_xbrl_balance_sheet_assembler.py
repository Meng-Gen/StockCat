#-*- coding: utf-8 -*-

from stockcat.assembler.xbrl.xbrl_balance_sheet_assembler import XbrlBalanceSheetAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class XbrlBalanceSheetAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = XbrlBalanceSheetAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None

    def test_assemble_2330_in_2014Q3(self):
        # online: http://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID=2330&SYEAR=2014&SSEASON=3&REPORT_ID=C
        path = './stockcat/tests/unit/data/xbrl_financial_statement/2330/2014/03.html'
        param = {
            'content' : self.file_utils.read_file(path),
            'stock_symbol' : '2330',
            'date' : datetime.date(2014, 9, 30),
        }
        dao = self.assembler.assemble(param)        
        
        column_name_list = dao.get_column_name_list()
        row_list = dao.get_row_list()

        self.assertEqual(column_name_list[0], u'會計項目')
        self.assertEqual(column_name_list[1], datetime.date(2014, 9, 30))
        self.assertEqual(column_name_list[2], datetime.date(2013, 12, 31))
        self.assertEqual(column_name_list[3], datetime.date(2013, 9, 30))     
        self.assertEqual(row_list[0], [u'資產'])
        self.assertEqual(row_list[1], [u'流動資產'])
        self.assertEqual(row_list[2], [u'現金及約當現金'])
        self.assertEqual(row_list[3], [u'現金及約當現金合計', 225884318, 242695447, 216603697])
