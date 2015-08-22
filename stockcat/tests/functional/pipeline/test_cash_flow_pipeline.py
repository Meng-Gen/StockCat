#-*- coding: utf-8 -*-

from stockcat.database.postgres_database_health_checker import PostgresDatabaseHealthChecker
from stockcat.pipeline.cash_flow_pipeline import CashFlowPipeline

import datetime
import unittest

class CashFlowPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = CashFlowPipeline()
        self.checker = PostgresDatabaseHealthChecker()

    def tearDown(self):
        self.pipeline = None
        self.checker = None

    # http://www.twse.com.tw/ch/trading/indices/twco/tai50i.php
    def test_run_taiwan_50_index(self):
        taiwan_50_index = [
            ('1301', datetime.date(2012, 3, 31)),
            ('2317', datetime.date(2011, 6, 30)),
            ('2330', datetime.date(2010, 9, 30)),
            ('2498', datetime.date(2014, 9, 30)),
            ('2474', datetime.date(2010, 12, 31)),
            ('2412', datetime.date(2013, 12, 31)),
            ('2357', datetime.date(2009, 3, 31)),   
        ]
        for stock_symbol, stmt_date in taiwan_50_index:
            entry = { 
                'table' : 'cash_flow',
                'stock_symbol' : stock_symbol, 
                'stmt_date' : stmt_date,
            }
            self.pipeline.avoid_blocking()
            self.pipeline.run(entry['stock_symbol'], entry['stmt_date'], ['spider', 'assembler', 'database'])
            self.checker.check_entry_existed(entry)

    @unittest.skip("skip long time functional tests")
    def test_run_many_2330_in_whole_2011(self):
        date_period = datetime.date(2011, 1, 1), datetime.date(2011, 12, 31)
        self.pipeline.run_many('2330', date_period, ['spider', 'assembler', 'database'])
