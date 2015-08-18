#-*- coding: utf-8 -*-

import psycopg2

class PostgresStoreCommand():
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def store_operating_revenue(self, feed):
        operation = 'INSERT INTO operating_revenue(release_date,stock_symbol,stmt_date,account,account_order,value) VALUES (%(release_date)s, %(stock_symbol)s, %(stmt_date)s, %(account)s, %(account_order)s, %(value)s)'
        self.__store_feed(operation, feed)

    def store_stock_symbol(self, feed):
        operation = 'INSERT INTO stock_symbol(release_date,stock_symbol,stock_name,isin_code,listing_date,market_category,industry_category,cfi_code) VALUES (%(release_date)s, %(stock_symbol)s, %(stock_name)s, %(isin_code)s, %(listing_date)s, %(market_category)s, %(industry_category)s, %(cfi_code)s)'
        self.__store_feed(operation, feed)

    def store_capital_increase_history(self, feed):
        operation = 'INSERT INTO capital_increase_history(release_date,stock_symbol,stmt_date,account,account_order,value) VALUES (%(release_date)s, %(stock_symbol)s, %(stmt_date)s, %(account)s, %(account_order)s, %(value)s)'
        self.__store_feed(operation, feed)

    def store_dividend_policy(self, feed):
        operation = 'INSERT INTO dividend_policy(release_date,stock_symbol,stmt_date,account,account_order,value) VALUES (%(release_date)s, %(stock_symbol)s, %(stmt_date)s, %(account)s, %(account_order)s, %(value)s)'
        self.__store_feed(operation, feed)

    def __store_feed(self, operation, feed):
        connection = psycopg2.connect(self.connection_string)
        cursor = connection.cursor()
        for entry in feed:
            try:
                cursor.execute(operation, entry)
            except psycopg2.IntegrityError:
                connection.rollback()
            else:
                connection.commit()
        cursor.close()
        connection.close()
