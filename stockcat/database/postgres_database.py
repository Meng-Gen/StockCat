#-*- coding: utf-8 -*-

from stockcat.database.postgres_get_command import PostgresGetCommnad
from stockcat.database.postgres_store_command import PostgresStoreCommand

class PostgresDatabase():
    def __init__(self, connection_string):
        self.store_command = PostgresStoreCommand(connection_string)
        self.get_command = PostgresGetCommnad(connection_string)

    def store_operating_revenue(self, feed):
        self.store_command.store_operating_revenue(feed)

    def store_stock_symbol(self, feed):
        self.store_command.store_stock_symbol(feed)

    def store_capital_increase_history(self, feed):
        self.store_command.store_capital_increase_history(feed)

    def store_dividend_policy(self, feed):
        self.store_command.store_dividend_policy(feed)

    def get_stock_symbol_list(self):
        return self.get_command.get_stock_symbol_list()