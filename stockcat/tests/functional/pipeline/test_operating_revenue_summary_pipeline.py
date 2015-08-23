#-*- coding: utf-8 -*-

from stockcat.database.postgres_database_health_checker import PostgresDatabaseHealthChecker
from stockcat.pipeline.operating_revenue_summary_pipeline import OperatingRevenueSummaryPipeline

import datetime
import unittest

class OperatingRevenueSummaryPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = OperatingRevenueSummaryPipeline()
        self.checker = PostgresDatabaseHealthChecker()

    def tearDown(self):
        self.pipeline = None
        self.checker = None
    
    def test_run_in_Feb_2013(self):
        entry = { 
            'table' : 'operating_revenue',
            'stock_symbol' : '1101', 
            'stmt_date' : datetime.date(2013, 2, 28),
        }
        self.pipeline.run(entry['stmt_date'], ['spider', 'assembler', 'database'])
        self.checker.check_entry_existed(entry)
