#-*- coding: utf-8 -*-

from stockcat.pipeline.dividend_policy_pipeline import DividendPolicyPipeline

import datetime
import unittest

class DividendPolicyPipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipeline = DividendPolicyPipeline()

    def tearDown(self):
        self.pipeline = None
    
    def test_run_2498(self):
        self.pipeline.run('2498', ['spider', 'assembler', 'database'])
