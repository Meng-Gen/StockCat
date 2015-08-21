#-*- coding: utf-8 -*-

from stockcat.database.postgres_database_health_checker import PostgresDatabaseHealthChecker
from stockcat.pipeline.balance_sheet_pipeline import BalanceSheetPipeline

import datetime
import unittest

class BalanceSheetPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = BalanceSheetPipeline()
        self.checker = PostgresDatabaseHealthChecker()

    def tearDown(self):
        self.pipeline = None
        self.checker = None

    def test_run_2330_in_2010Q3(self):
        entry = { 
            'table' : 'balance_sheet',
            'stock_symbol' : '2330', 
            'stmt_date' : datetime.date(2010, 9, 30),
        }
        self.pipeline.run(entry['stock_symbol'], entry['stmt_date'], ['spider', 'assembler', 'database'])
        self.checker.check_entry_existed(entry)

    def test_run_2330_in_2014Q3(self):
        entry = { 
            'table' : 'balance_sheet',
            'stock_symbol' : '2330', 
            'stmt_date' : datetime.date(2014, 9, 30),
        }
        self.pipeline.run(entry['stock_symbol'], entry['stmt_date'], ['spider', 'assembler', 'database'])
        self.checker.check_entry_existed(entry)

    @unittest.skip("skip long time functional tests")
    def test_run_many_2330_in_2011(self):
        date_period = datetime.date(2011, 1, 1), datetime.date(2011, 12, 31)
        self.pipeline.run_many('2330', date_period, ['spider', 'assembler', 'database'])
