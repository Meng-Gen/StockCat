#-*- coding: utf-8 -*-

from stockcat.pipeline.capital_increase_history_pipeline import CapitalIncreaseHistoryPipeline

import datetime
import unittest

class CapitalIncreaseHistoryPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = CapitalIncreaseHistoryPipeline()

    def tearDown(self):
        self.pipeline = None
    
    def test_run_2498(self):
        self.pipeline.run('2498', ['spider', 'assembler', 'database'])
