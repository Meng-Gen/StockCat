#-*- coding: utf-8 -*-

from stockcat.database.postgres_get_command import PostgresGetCommnad
from stockcat.database.postgres_store_command import PostgresStoreCommand

class PostgresDatabase():
    def __init__(self, connection_string):
        self.store_command = PostgresStoreCommand(connection_string)
        self.get_command = PostgresGetCommnad(connection_string)

    def store(self, feed):
        return self.store_command.store(feed)

    def store_operating_revenue(self, feed):
        self.store_command.store_operating_revenue(feed)

    def store_stock_symbol(self, feed):
        self.store_command.store_stock_symbol(feed)

    def store_capital_increase_history(self, feed):
        self.store_command.store_capital_increase_history(feed)

    def store_dividend_policy(self, feed):
        self.store_command.store_dividend_policy(feed)

    def store_balance_sheet(self, feed):
        self.store_command.store_balance_sheet(feed)

    def store_income_statement(self, feed):
        self.store_command.store_income_statement(feed)

    def store_cash_flow(self, feed):
        self.store_command.store_cash_flow(feed)

    def get_stock_symbol_list(self):
        return self.get_command.get_stock_symbol_list()

    def get_capital_increase_by_cash(self, stock_symbol):
        return self.get_command.get_capital_increase_by_cash(stock_symbol)

    def get_capital_increase_by_earnings(self, stock_symbol):
        return self.get_command.get_capital_increase_by_earnings(stock_symbol)

    def get_capital_increase_by_surplus(self, stock_symbol):
        return self.get_command.get_capital_increase_by_surplus(stock_symbol)
