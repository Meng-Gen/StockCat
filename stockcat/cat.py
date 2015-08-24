#-*- coding: utf-8 -*-

import logging

class Cat():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.run_stock_symbol()
        self.run_operating_revenue()

    def run_stock_symbol(self):
        from stockcat.state.stock_symbol.state_machine import StateMachine
        state_machine = StateMachine()
        state_machine.run()

    def run_operating_revenue(self):
        from stockcat.state.operating_revenue.state_machine import StateMachine
        state_machine = StateMachine()
        state_machine.run()