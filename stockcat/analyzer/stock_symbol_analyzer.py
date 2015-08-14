#-*- coding: utf-8 -*-

from stockcat.database.database import Database

class StockSymbolAnalyzer():
    def __init__(self):
        self.database = Database()

    def analyze(self):
        return self.database.get_stock_symbol()
