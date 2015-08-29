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
        return [{ 'stock_symbol' : record[0], 'listing_date' : record[1] } for record in records]

    def get_capital_increase_by_cash(self, stock_symbol):
        connection = psycopg2.connect(self.connection_string)
        cursor = connection.cursor()
        entry = { 'stock_symbol' : stock_symbol }
        cursor.execute(u"select stock_symbol, stmt_date, value from capital_increase_history where release_date in (select max(release_date) from stock_symbol) and stock_symbol = %(stock_symbol)s and account = '現金增資' order by stmt_date", entry)
        records = cursor.fetchall()
        connection.commit()
        connection.close()
        return records

    def get_capital_increase_by_earnings(self, stock_symbol):
        connection = psycopg2.connect(self.connection_string)
        cursor = connection.cursor()
        entry = { 'stock_symbol' : stock_symbol }
        cursor.execute(u"select stock_symbol, stmt_date, value from capital_increase_history where release_date in (select max(release_date) from stock_symbol) and stock_symbol = %(stock_symbol)s and account = '盈餘轉增資' order by stmt_date", entry)
        records = cursor.fetchall()
        connection.commit()
        connection.close()
        return records

    def get_capital_increase_by_surplus(self, stock_symbol):
        connection = psycopg2.connect(self.connection_string)
        cursor = connection.cursor()
        entry = { 'stock_symbol' : stock_symbol }
        cursor.execute(u"select stock_symbol, stmt_date, value from capital_increase_history where release_date in (select max(release_date) from stock_symbol) and stock_symbol = %(stock_symbol)s and account = '公積及其他' order by stmt_date", entry)
        records = cursor.fetchall()
        connection.commit()
        connection.close()
        return records