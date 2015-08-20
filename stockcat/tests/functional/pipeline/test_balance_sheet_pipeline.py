#-*- coding: utf-8 -*-

from stockcat.pipeline.balance_sheet_pipeline import BalanceSheetPipeline

import datetime
import unittest

class BalanceSheetPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = BalanceSheetPipeline()

    def tearDown(self):
        self.pipeline = None

    def test_run_2330_in_2010Q3(self):
        self.pipeline.run('2330', datetime.date(2010, 9, 30), ['spider', 'assembler', 'database'])

    def test_run_2330_in_2014Q3(self):
        self.pipeline.run('2330', datetime.date(2014, 9, 30), ['spider', 'assembler', 'database'])
        #self.pipeline.run('2330', datetime.date(2014, 9, 30), ['assembler', 'database'])

    @unittest.skip("skip long time functional tests")
    def test_run_many_2330_in_2011(self):
        date_period = datetime.date(2011, 1, 1), datetime.date(2011, 12, 31)
        self.pipeline.run_many('2330', date_period, ['spider', 'assembler', 'database'])
