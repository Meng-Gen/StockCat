#-*- coding: utf-8 -*-

from stockcat.pipeline.stock_symbol_pipeline import StockSymbolPipeline
from stockcat.pipeline.operating_revenue_pipeline import OperatingRevenuePipeline
from stockcat.pipeline.dividend_policy_pipeline import DividendPolicyPipeline
from stockcat.pipeline.capital_increase_history_pipeline import CapitalIncreaseHistoryPipeline
from stockcat.pipeline.balance_sheet_pipeline import BalanceSheetPipeline
from stockcat.pipeline.income_statement_pipeline import IncomeStatementPipeline
from stockcat.pipeline.cash_flow_pipeline import CashFlowPipeline

import logging

class StockCat():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        #self.run_stock_symbol()
        #self.run_operating_revenue()
        #self.run_dividend_policy()
        #self.run_capital_increase_history()
        #self.run_balance_sheet()
        #self.run_income_statement()
        self.run_cash_flow()

    def run_stock_symbol(self):
        StockSymbolPipeline().run()

    def run_operating_revenue(self):
        OperatingRevenuePipeline().run()

    def run_dividend_policy(self):
        DividendPolicyPipeline().run()

    def run_capital_increase_history(self):
        CapitalIncreaseHistoryPipeline().run()

    def run_balance_sheet(self):
        BalanceSheetPipeline().run()

    def run_income_statement(self):
        IncomeStatementPipeline().run()

    def run_cash_flow(self):
        CashFlowPipeline().run()
