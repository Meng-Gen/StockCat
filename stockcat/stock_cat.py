#-*- coding: utf-8 -*-

import logging

class StockCat():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.run_stock_symbol()
        #self.run_operating_revenue()
        #self.run_dividend_policy()
        #self.run_capital_increase_history()

    def run_stock_symbol(self):
        from stockcat.state.stock_symbol.state_machine import StateMachine
        StateMachine().run()

    def run_operating_revenue(self):
        from stockcat.state.operating_revenue.state_machine import StateMachine
        StateMachine().run()

    def run_dividend_policy(self):
        from stockcat.state.dividend_policy.state_machine import StateMachine
        StateMachine().run()

    def run_capital_increase_history(self):
        from stockcat.state.capital_increase_history.state_machine import StateMachine
        StateMachine().run()

    def debug_default_memento(self):
        from stockcat.state.stock_symbol.state_machine import StateMachine
        self.logger.info('stock_symbol: {0}'.format(StateMachine().memento.get_default_value()))

        from stockcat.state.operating_revenue.state_machine import StateMachine
        self.logger.info('operating_revenue: {0}'.format(StateMachine().memento.get_default_value()))
