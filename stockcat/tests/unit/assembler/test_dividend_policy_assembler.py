#-*- coding: utf-8 -*-

from stockcat.assembler.assemble_error import NoRecordAssembleError
from stockcat.assembler.dividend_policy_assembler import DividendPolicyAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class StockCapitalIncreaseHistoryAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = DividendPolicyAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None
    
    def test_assemble_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcc/zcc_2498.djhtm
        content = self.file_utils.read_file('./stockcat/tests/unit/data/dividend_policy/2498.html')
        dao = self.assembler.assemble(content, '2498')

        self.assertEqual(dao.get_stock_symbol(), '2498')

        actual = dao.get_column_name_list()
        expected = [u'年度', u'現金股利', u'盈餘配股', u'公積配股', u'股票股利', u'合計', u'員工配股率%']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [datetime.date(2014, 12, 31), 0.38, 0, 0, 0, 0.38, 0.0000])
        self.assertEqual(row_list[4], [datetime.date(2010, 12, 31), 37, 0.5000000092, 0, 0.5000000092, 37.5000000092, 0.0050])
        for row in row_list:
            self.assertEqual(len(row), 7)

    def test_assemble_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcc/zcc_3009.djhtm
        content = self.file_utils.read_file('./stockcat/tests/unit/data/error/dividend_policy_not_found_error.html')
        with self.assertRaises(NoRecordAssembleError) as context:
            self.assembler.assemble(content, '3009')
        self.assertEqual(context.exception.param['stock_symbol'], '3009')   
