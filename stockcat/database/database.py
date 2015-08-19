#-*- coding: utf-8 -*-

from stockcat.database.postgres_database import PostgresDatabase

class Database():
    def __init__(self):
        self.impl = PostgresDatabase("dbname='stockcat' user='stockcat' host='localhost' password='stockcat'")

    def store(self, feed):
        return self.impl.store(feed)

    def store_operating_revenue(self, feed):
        return self.impl.store_operating_revenue(feed)

    def store_stock_symbol(self, feed):
        return self.impl.store_stock_symbol(feed)

    def store_capital_increase_history(self, feed):
        return self.impl.store_capital_increase_history(feed)

    def store_dividend_policy(self, feed):
        return self.impl.store_dividend_policy(feed)

    def store_balance_sheet(self, feed):
        return self.impl.store_balance_sheet(feed)

    def store_income_statement(self, feed):
        return self.impl.store_income_statement(feed)

    def store_cash_flow(self, feed):
        return self.impl.store_cash_flow(feed)

    def get_stock_symbol_list(self):
        return self.impl.get_stock_symbol_list()

    def get_capital_increase_by_cash(self, stock_symbol):
        return self.impl.get_capital_increase_by_cash(stock_symbol)

    def get_capital_increase_by_earnings(self, stock_symbol):
        return self.impl.get_capital_increase_by_earnings(stock_symbol)

    def get_capital_increase_by_surplus(self, stock_symbol):
        return self.impl.get_capital_increase_by_surplus(stock_symbol)
