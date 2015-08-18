#-*- coding: utf-8 -*-

from stockcat.database.database import Database

class CapitalIncreaseHistoryAnalyzer():
    def __init__(self):
        self.database = Database()

    def get_capital_increase_by_cash(self, stock_symbol):
        return self.database.get_capital_increase_by_cash(stock_symbol)

    def get_capital_increase_by_earnings(self, stock_symbol):
        return self.database.get_capital_increase_by_earnings(stock_symbol)

    def get_capital_increase_by_surplus(self, stock_symbol):
        return self.database.get_capital_increase_by_surplus(stock_symbol)
