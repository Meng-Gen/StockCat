#-*- coding: utf-8 -*-

from stockcat.database.postgres_database_health_checker import PostgresDatabaseHealthChecker
from stockcat.pipeline.stock_symbol_pipeline import StockSymbolPipeline

import unittest

class StockSymbolPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = StockSymbolPipeline()
        self.checker = PostgresDatabaseHealthChecker()

    def tearDown(self):
        self.pipeline = None
        self.checker = None

    def test_run(self):
        self.pipeline.run(['spider', 'assembler', 'database'])
        self.checker.check_entry_existed({
            'table' : 'stock_symbol',
            'market_category' : u'上市',
            'cfi_code' : u'ESVUFR',
        })
        self.checker.check_entry_existed({
            'table' : 'stock_symbol',
            'market_category' : u'上櫃',
            'cfi_code' : u'ESVUFR',
        })
