#-*- coding: utf-8 -*-

from stockcat.pipeline.cash_flow_pipeline import CashFlowPipeline

import datetime
import unittest

class CashFlowPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = CashFlowPipeline()

    def tearDown(self):
        self.pipeline = None
    
    def test_run_2498_in_2009Q4(self):
        self.pipeline.run('2498', datetime.date(2009, 12, 31), ['spider', 'assembler', 'database'])

    """
    def test_run_2330_in_2010Q3(self):
        self.pipeline.run('2330', datetime.date(2010, 9, 30), ['spider', 'assembler', 'database'])

    def test_run_2330_in_2011Q2(self):
        self.pipeline.run('2330', datetime.date(2011, 6, 30), ['spider', 'assembler', 'database'])
    
    def test_run_many_2330_in_whole_2011(self):
        date_period = datetime.date(2011, 1, 1), datetime.date(2011, 12, 31)
        self.pipeline.run_many('2330', date_period, ['spider', 'assembler', 'database'])
    """
