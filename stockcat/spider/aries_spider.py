#-*- coding: utf-8 -*-

from stockcat.spider.storage.spider_storage import SpiderStorage
from stockcat.common.string_utils import StringUtils

class AriesSpider():
    def __init__(self):
        self.storage = SpiderStorage()
        self.string_utils = StringUtils()
        
    def crawl(self, stock_symbol, date):
        params = self.__parse_params(stock_symbol, date)
        url = self.build_url(params)
        key = self.build_key(params)
        self.storage.set(key, url)

    def is_crawled(self, stock_symbol, date):
        params = self.__parse_params(stock_symbol, date)
        key = self.build_key(params)
        return self.storage.contains(key)

    def get_crawled(self, stock_symbol, date):
        params = self.__parse_params(stock_symbol, date)
        key = self.build_key(params)
        return self.storage.get(key)

    def __parse_params(self, stock_symbol, date):
        return {
            'stock_symbol' : stock_symbol,
            'roc_era' : self.string_utils.from_date_to_roc_era_string(date),
            'year' : str(date.year),
            'quarter' : self.string_utils.from_date_to_2_digit_quarter_string(date),
            'quarter_xbrl' : self.string_utils.from_date_to_1_digit_quarter_string(date),
            'month' : self.string_utils.from_date_to_2_digit_month_string(date),
        }

    def build_url(self, params):
        raise NotImplementedError

    def build_key(self, params):
        raise NotImplementedError