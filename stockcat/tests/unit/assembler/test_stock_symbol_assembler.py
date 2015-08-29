#-*- coding: utf-8 -*-

from stockcat.assembler.stock_symbol_assembler import StockSymbolAssembler
from stockcat.common.file_utils import FileUtils
from stockcat.dao.operating_revenue_dao import OperatingRevenueDao

import datetime
import unittest

class StockSymbolAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = StockSymbolAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None
    
    def test_assemble_stock_exchange_market(self):
        # online: http://isin.twse.com.tw/isin/C_public.jsp?strMode=2 
        path = './stockcat/tests/unit/data/stock_symbol/stock_exchange_market.html'
        param = { 'content' : self.file_utils.read_file(path) }
        dao = self.assembler.assemble(param)

        actual = dao.get_column_name_list()
        expected = [u'有價證券代號', u'名稱', u'國際證券辨識號碼(ISIN Code)', u'上市日', u'市場別', u'產業別', u'CFICode', u'備註']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'1101', u'台泥', u'TW0001101004', datetime.date(1962, 2, 9), u'上市', u'水泥工業', u'ESVUFR', u''])
        for row in row_list:
            self.assertEqual(len(row), 8)

        self.assertEqual(dao.get_release_date(), datetime.date(2015, 8, 7))

    def test_assemble_otc_market(self):
        # online: http://isin.twse.com.tw/isin/C_public.jsp?strMode=4
        path = './stockcat/tests/unit/data/stock_symbol/otc_market.html'
        param = { 'content' : self.file_utils.read_file(path) }
        dao = self.assembler.assemble(param)

        actual = dao.get_column_name_list()
        expected = [u'有價證券代號', u'名稱', u'國際證券辨識號碼(ISIN Code)', u'上市日', u'市場別', u'產業別', u'CFICode', u'備註']
        self.assertEqual(actual, expected)

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'5364', u'力麗店', u'TW0005364004', datetime.date(2013, 8, 26), u'上櫃', u'其他業', u'ESVUFR', u''])
        for row in row_list:
            self.assertEqual(len(row), 8)

        self.assertEqual(dao.get_release_date(), datetime.date(2015, 8, 7))
