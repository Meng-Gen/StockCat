#-*- coding: utf-8 -*-

from stockcat.database.postgres_database import PostgresDatabase

class Database():
    def __init__(self):
        self.impl = PostgresDatabase("dbname='stockcat' user='stockcat' host='localhost' password='stockcat'")

    def store_operating_revenue(self, feed):
        return self.impl.store_operating_revenue(feed)
