#-*- coding: utf-8 -*-

from stockcat.database.database import Database

import datetime
import unittest

class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.database = Database()

    def tearDown(self):
        self.database = None
    
    def test_get_stock_symbol_list(self):
        stock_symbol_list = self.database.get_stock_symbol_list()
        self.assertEqual(stock_symbol_list[0], ('1101', datetime.date(1962, 2, 9)))
        self.assertEqual(stock_symbol_list[1], ('1102', datetime.date(1962, 6, 8)))
