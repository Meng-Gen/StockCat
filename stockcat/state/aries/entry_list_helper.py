#-*- coding: utf-8 -*-

from stockcat.analyzer.stock_symbol_analyzer import StockSymbolAnalyzer
from stockcat.common.date_utils import DateUtils

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