#-*- coding: utf-8 -*-

from stockcat.pipeline.income_statement_pipeline import IncomeStatementPipeline

import datetime
import unittest

class IncomeStatementPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = IncomeStatementPipeline()

    def tearDown(self):
        self.pipeline = None
    
    def test_run_2330_in_2010Q3(self):
        self.pipeline.run('2330', datetime.date(2010, 9, 30), ['spider', 'assembler', 'database'])

    @unittest.skip("skip long time functional tests")
    def test_run_many_2330_in_2011(self):
        date_period = datetime.date(2011, 1, 1), datetime.date(2011, 12, 31)
        self.pipeline.run_many('2330', date_period, ['spider', 'assembler', 'database'])
