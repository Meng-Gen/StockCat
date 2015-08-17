#-*- coding: utf-8 -*-

from stockcat.assembler.assemble_error import NoRecordAssembleError
from stockcat.assembler.capital_increase_history_assembler import CapitalIncreaseHistoryAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class StockCapitalIncreaseHistoryAssembler(unittest.TestCase):
    def setUp(self):
        self.assembler = CapitalIncreaseHistoryAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None
    
    def test_assemble_2498(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcb/zcb_2498.djhtm
        content = self.file_utils.read_file('./stockcat/tests/unit/data/capital_increase_history/2498.html')
        dao = self.assembler.assemble(content, '2498')

        self.assertEqual(dao.get_stock_symbol(), '2498')

        actual = dao.get_column_name_list()
        expected = [u'年度', u'現金增資', u'比重', u'盈餘轉增資', u'比重', u'公積及其他', u'比重']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [datetime.date(2015, 12, 31), 14.464519, 0.1747, 67.724067, 0.8180, 0.598634, 0.0072])
        for row in row_list:
            self.assertEqual(len(row), 7)

    def test_assemble_raise_no_record_assemble_error(self):
        # online: http://jdata.yuanta.com.tw/z/zc/zcb/zcb_3009.djhtm
        content = self.file_utils.read_file('./stockcat/tests/unit/data/error/capital_increase_history_not_found_error.html')
        with self.assertRaises(NoRecordAssembleError) as context:
            self.assembler.assemble(content, '3009')
        self.assertEqual(context.exception.param['stock_symbol'], '3009')   
