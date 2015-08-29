#-*- coding: utf-8 -*-

from stockcat.analyzer.stock_symbol_analyzer import StockSymbolAnalyzer

import datetime
import unittest

class StockSymbolAnalyzerTest(unittest.TestCase):
    def setUp(self):
        self.analyzer = StockSymbolAnalyzer()

    def tearDown(self):
        self.analyzer = None
    
    def test_get_stock_symbol_list(self):
        stock_symbol_list = self.analyzer.get_stock_symbol_list()
        self.assertEqual(stock_symbol_list[0], {'stock_symbol' : '1101', 'listing_date' : datetime.date(1962, 2, 9)})
        self.assertEqual(stock_symbol_list[1], {'stock_symbol' : '1102', 'listing_date' : datetime.date(1962, 6, 8)})
