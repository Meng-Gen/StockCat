#-*- coding: utf-8 -*-

from stockcat.database.postgres_get_command import PostgresGetCommnad
from stockcat.database.postgres_store_command import PostgresStoreCommand

class PostgresDatabase():
    def __init__(self, connection_string):
        self.store_command = PostgresStoreCommand(connection_string)
        self.get_command = PostgresGetCommnad(connection_string)

    def store(self, feed):
        return self.store_command.store(feed)

    def get_stock_symbol_list(self):
        return self.get_command.get_stock_symbol_list()

    def get_capital_increase_by_cash(self, stock_symbol):
        return self.get_command.get_capital_increase_by_cash(stock_symbol)

    def get_capital_increase_by_earnings(self, stock_symbol):
        return self.get_command.get_capital_increase_by_earnings(stock_symbol)

    def get_capital_increase_by_surplus(self, stock_symbol):
        return self.get_command.get_capital_increase_by_surplus(stock_symbol)
