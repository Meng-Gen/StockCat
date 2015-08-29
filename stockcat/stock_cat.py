#-*- coding: utf-8 -*-

from stockcat.state.stock_symbol_state_machine import StockSymbolStateMachine
from stockcat.state.operating_revenue_state_machine import OperatingRevenueStateMachine
from stockcat.state.dividend_policy_state_machine import DividendPolicyStateMachine
from stockcat.state.capital_increase_history_state_machine import CapitalIncreaseHistoryStateMachine


import logging

class StockCat():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.run_stock_symbol()
        self.run_operating_revenue()
        self.run_dividend_policy()
        self.run_capital_increase_history()

    def run_stock_symbol(self):
        StockSymbolStateMachine().run()

    def run_operating_revenue(self):
        OperatingRevenueStateMachine().run()

    def run_dividend_policy(self):
        DividendPolicyStateMachine().run()

    def run_capital_increase_history(self):
        CapitalIncreaseHistoryStateMachine().run()
