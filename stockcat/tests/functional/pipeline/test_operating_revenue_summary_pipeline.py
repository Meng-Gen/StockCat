#-*- coding: utf-8 -*-

from stockcat.pipeline.operating_revenue_summary_pipeline import OperatingRevenueSummaryPipeline

import datetime
import unittest

class OperatingRevenueSummaryPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = OperatingRevenueSummaryPipeline()

    def tearDown(self):
        self.pipeline = None
    
    def test_run_many_from_July_2015_to_July_2015(self):
        date_period = datetime.date(2015, 7, 1), datetime.date(2015, 7, 31)
        self.pipeline.run_many(date_period, ['spider', 'assembler', 'database'])        
