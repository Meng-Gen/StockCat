#-*- coding: utf-8 -*-

from stockcat.analyzer.stock_symbol_analyzer import StockSymbolAnalyzer
from stockcat.common.date_utils import DateUtils

import datetime
import itertools
import logging

class EntryListHelper():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_stock_symbol_list(self):
        return StockSymbolAnalyzer().get_stock_symbol_list()

    def get_now_date(self):
        return DateUtils().now_date()

    def get_date_list_by_month(self, begin_date, end_date):
        output = []
        for date in DateUtils().range_date_by_month(begin_date, end_date):
            output.append({ 'date' : date })
        return output

    def get_date_list_by_quarter(self, begin_date, end_date):
        output = []
        for date in DateUtils().range_date_by_quarter(begin_date, end_date):
            output.append({ 'date' : date })
        return output

    def get_market_type_list(self):
        return [
            { 'market_type' : 'stock_exchange_market' },
            { 'market_type' : 'otc_market' },            
        ]

    def product(self, one_list, other_list):
        output = []
        for x, y in itertools.product(one_list, other_list):
            z = dict(x)
            z.update(y)
            output.append(z)
        return output

    def get_operating_revenue_entry_list(self):
        begin_date = datetime.date(2010, 6, 30)
        end_date = self.get_now_date()
        date_list = self.get_date_list_by_month(begin_date, end_date)
        market_type_list = self.get_market_type_list()
        return self.product(date_list, market_type_list)

    def get_all_financial_statement_entry_list(self):
        entry_list = []
        site_begin_date = datetime.date(1996, 3, 31)
        end_date = self.get_now_date()
        for stock_symbol in self.get_stock_symbol_list():
            begin_date = max(site_begin_date, stock_symbol['listing_date'])
            for date in self.get_date_list_by_quarter(begin_date, end_date):
                entry = {
                    'stock_symbol' : stock_symbol['stock_symbol'],
                    'date' : date['date'],
                }
                entry_list.append(entry)
        return entry_list

    def get_legacy_financial_statement_entry_list(self):
        entry_list = []
        site_begin_date = datetime.date(1996, 3, 31)
        end_date = datetime.date(2012, 12, 31)
        for stock_symbol in self.get_stock_symbol_list():
            begin_date = max(site_begin_date, stock_symbol['listing_date'])
            for date in self.get_date_list_by_quarter(begin_date, end_date):
                entry = {
                    'stock_symbol' : stock_symbol['stock_symbol'],
                    'date' : date['date'],
                }
                entry_list.append(entry)
        return entry_list