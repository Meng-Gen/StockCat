#-*- coding: utf-8 -*-

from stockcat.database.postgres_database import PostgresDatabase

class Database():
    def __init__(self):
        self.impl = PostgresDatabase("dbname='stockcat' user='stockcat' host='localhost' password='stockcat'")

    def store(self, feed):
        return self.impl.store(feed)

    def get_stock_symbol_list(self):
        return self.impl.get_stock_symbol_list()

    def get_capital_increase_by_cash(self, stock_symbol):
        return self.impl.get_capital_increase_by_cash(stock_symbol)

    def get_capital_increase_by_earnings(self, stock_symbol):
        return self.impl.get_capital_increase_by_earnings(stock_symbol)

    def get_capital_increase_by_surplus(self, stock_symbol):
        return self.impl.get_capital_increase_by_surplus(stock_symbol)
