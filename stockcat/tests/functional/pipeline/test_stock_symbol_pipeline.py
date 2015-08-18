#-*- coding: utf-8 -*-

from stockcat.pipeline.stock_symbol_pipeline import StockSymbolPipeline

import datetime
import unittest

class StockSymbolPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = StockSymbolPipeline()

    def tearDown(self):
        self.pipeline = None
    
    def test_run(self):
        self.pipeline.run(['spider', 'assembler', 'database'])
