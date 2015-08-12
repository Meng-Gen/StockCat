#-*- coding: utf-8 -*-

from stockcat.database.database import Database

class StockSymbolAnalyzer():
    def __init__(self):
        self.database = Database()

    def analyze(self):
        # TODO: select stock_symbol, listing_date from stock_symbol where cfi_code = 'ESVUFR';
        pass