#-*- coding: utf-8 -*-

import psycopg2

class PostgresGetCommnad():
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def get_stock_symbol_list(self):
        connection = psycopg2.connect(self.connection_string)
        cursor = connection.cursor()
        cursor.execute("select stock_symbol, listing_date from stock_symbol where release_date in (select max(release_date) from stock_symbol) and cfi_code = 'ESVUFR'")
        records = cursor.fetchall()
        connection.commit()
        connection.close()
        return records
