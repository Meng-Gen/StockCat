#-*- coding: utf-8 -*-

import psycopg2

class PostgresDatabase():
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def store_operating_revenue(self, feed):
        connection = psycopg2.connect(self.connection_string)
        cursor = connection.cursor()
        for entry in feed:
            cursor.execute('INSERT INTO operating_revenue(release_date,stock_symbol,stmt_date,account,account_order,value) VALUES (%(release_date)s, %(stock_symbol)s, %(stmt_date)s, %(account)s, %(account_order)s, %(value)s)', entry)
        connection.commit()
        connection.close()
