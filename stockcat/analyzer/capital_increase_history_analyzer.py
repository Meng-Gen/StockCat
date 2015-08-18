#-*- coding: utf-8 -*-

from stockcat.database.database import Database

class CapitalIncreaseHistoryAnalyzer():
    def __init__(self):
        self.database = Database()

    def get_stock_symbol_list(self):
        return self.database.get_stock_symbol_list()
