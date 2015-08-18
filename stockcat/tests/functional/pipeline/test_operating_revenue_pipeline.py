#-*- coding: utf-8 -*-

from stockcat.pipeline.operating_revenue_pipeline import OperatingRevenuePipeline

import datetime
import unittest

# Supplementary for operating revenue
class OperatingRevenuePipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = OperatingRevenuePipeline()

    def tearDown(self):
        self.pipeline = None
    
    def test_run_2330_for_one_month(self):
        self.pipeline.run('2330', datetime.date(2010, 1, 1), ['spider', 'assembler', 'database'])

    def test_run_many_2330_for_three_month(self):
        date_period = datetime.date(2010, 1, 1), datetime.date(2010, 3, 31)
        self.pipeline.run_many('2330', date_period, ['spider', 'assembler', 'database'])
