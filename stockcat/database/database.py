#-*- coding: utf-8 -*-

from stockcat.database.postgres_database import PostgresDatabase

class Database():
    def __init__(self):
        self.impl = PostgresDatabase("dbname='stockcat' user='stockcat' host='localhost' password='stockcat'")

    def store_operating_revenue(self, feed):
        return self.impl.store_operating_revenue(feed)

    def store_stock_symbol(self, feed):
        return self.impl.store_stock_symbol(feed)

    def store_capital_increase_history(self, feed):
        return self.impl.store_capital_increase_history(feed)

    def get_stock_symbol(self):
        return self.impl.get_stock_symbol()
