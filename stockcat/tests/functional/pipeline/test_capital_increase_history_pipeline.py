#-*- coding: utf-8 -*-

from stockcat.database.database_error import NoEntryDatabaseError
from stockcat.database.postgres_database_health_checker import PostgresDatabaseHealthChecker
from stockcat.pipeline.capital_increase_history_pipeline import CapitalIncreaseHistoryPipeline

import datetime
import unittest

class CapitalIncreaseHistoryPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = CapitalIncreaseHistoryPipeline()
        self.checker = PostgresDatabaseHealthChecker()

    def tearDown(self):
        self.pipeline = None
        self.checker = None
    
    def test_run_2330(self):
        entry = {
            'table' : 'capital_increase_history',
            'stock_symbol' : '2330',
        }
        self.pipeline.run(entry['stock_symbol'], ['spider', 'assembler', 'database'])
        self.checker.check_entry_existed(entry)

    def test_run_2498(self):
        entry = {
            'table' : 'capital_increase_history',
            'stock_symbol' : '2498',
        }
        self.pipeline.run(entry['stock_symbol'], ['spider', 'assembler', 'database'])
        self.checker.check_entry_existed(entry)        

    def test_run_3009(self):
        entry = {
            'table' : 'capital_increase_history',
            'stock_symbol' : '3009',
        }
        self.pipeline.run(entry['stock_symbol'], ['spider', 'assembler', 'database'])
        with self.assertRaises(NoEntryDatabaseError) as context:
            self.checker.check_entry_existed(entry)
        self.assertEqual(context.exception.param['stock_symbol'], '3009')
        