#-*- coding: utf-8 -*-

import psycopg2

class PostgresStoreCommand():
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.operation_map = {
            'StockSymbolFeed' : 'INSERT INTO stock_symbol(release_date,stock_symbol,stock_name,isin_code,listing_date,market_category,industry_category,cfi_code) VALUES (%(release_date)s, %(stock_symbol)s, %(stock_name)s, %(isin_code)s, %(listing_date)s, %(market_category)s, %(industry_category)s, %(cfi_code)s)',
            'BalanceSheetFeed' : 'INSERT INTO balance_sheet(release_date,stock_symbol,stmt_date,account,account_order,value) VALUES (%(release_date)s, %(stock_symbol)s, %(stmt_date)s, %(account)s, %(account_order)s, %(value)s)', 
            'IncomeStatementFeed' : 'INSERT INTO income_statement(release_date,stock_symbol,stmt_date,account,account_order,value) VALUES (%(release_date)s, %(stock_symbol)s, %(stmt_date)s, %(account)s, %(account_order)s, %(value)s)',
            'CashFlowFeed' : 'INSERT INTO cash_flow(release_date,stock_symbol,stmt_date,account,account_order,value) VALUES (%(release_date)s, %(stock_symbol)s, %(stmt_date)s, %(account)s, %(account_order)s, %(value)s)',
            'OperatingRevenueFeed' : 'INSERT INTO operating_revenue(release_date,stock_symbol,stmt_date,account,account_order,value) VALUES (%(release_date)s, %(stock_symbol)s, %(stmt_date)s, %(account)s, %(account_order)s, %(value)s)',
            'CapitalIncreaseHistoryFeed' : 'INSERT INTO capital_increase_history(release_date,stock_symbol,stmt_date,account,account_order,value) VALUES (%(release_date)s, %(stock_symbol)s, %(stmt_date)s, %(account)s, %(account_order)s, %(value)s)',
            'DividendPolicyFeed' : 'INSERT INTO dividend_policy(release_date,stock_symbol,stmt_date,account,account_order,value) VALUES (%(release_date)s, %(stock_symbol)s, %(stmt_date)s, %(account)s, %(account_order)s, %(value)s)',
        }

    def store(self, feed):
        operation = self.__get_operation(feed.__class__.__name__)
        self.__store_feed(operation, feed.get())

    def __get_operation(self, feed_class_name):
        return self.operation_map[feed_class_name]

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
