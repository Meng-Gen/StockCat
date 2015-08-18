#-*- coding: utf-8 -*-

from stockcat.analyzer.capital_increase_history_analyzer import CapitalIncreaseHistoryAnalyzer

import datetime
import unittest

class CapitalIncreaseHistoryAnalyzerTest(unittest.TestCase):
    def setUp(self):
        self.analyzer = CapitalIncreaseHistoryAnalyzer()

    def tearDown(self):
        self.analyzer = None
    
    def test_get_capital_increase_by_cash_of_2498(self):
        capital_increase = self.analyzer.get_capital_increase_by_cash('2498')
        self.assertEqual(capital_increase[0], ('2498', datetime.date(1997, 12, 31), 0.05))
        self.assertEqual(capital_increase[1], ('2498', datetime.date(1998, 12, 31), 10.0))

    def test_get_capital_increase_by_earnings_of_2498(self):
        capital_increase = self.analyzer.get_capital_increase_by_earnings('2498')
        self.assertEqual(capital_increase[0], ('2498', datetime.date(1997, 12, 31), 0))
        self.assertEqual(capital_increase[1], ('2498', datetime.date(1998, 12, 31), 0))
        self.assertEqual(capital_increase[4], ('2498', datetime.date(2002, 12, 31), 3.512))

    def test_get_capital_increase_by_surplus_of_2498(self):
        capital_increase = self.analyzer.get_capital_increase_by_surplus('2498')
        self.assertEqual(capital_increase[0], ('2498', datetime.date(1997, 12, 31), 0))
        self.assertEqual(capital_increase[1], ('2498', datetime.date(1998, 12, 31), 0))
        self.assertEqual(capital_increase[4], ('2498', datetime.date(2002, 12, 31), 0))
