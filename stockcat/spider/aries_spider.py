#-*- coding: utf-8 -*-

from stockcat.spider.storage.spider_storage import SpiderStorage
from stockcat.common.string_utils import StringUtils

class AriesSpider():
    def __init__(self):
        self.storage = SpiderStorage()
        self.string_utils = StringUtils()
        
    def crawl(self, param):
        param = self.__extend_param(param)
        url = self.build_url(param)
        key = self.build_key(param)
        self.storage.set(key, url)

    def is_crawled(self, param):
        param = self.__extend_param(param)
        key = self.build_key(param)
        return self.storage.contains(key)

    def get_crawled(self, param):
        param = self.__extend_param(param)
        key = self.build_key(param)
        return self.storage.get(key)

    def __extend_param(self, param):
        stock_symbol = param['stock_symbol']
        date = param['date']
        return {
            'stock_symbol' : stock_symbol,
            'roc_era' : self.string_utils.from_date_to_roc_era_string(date),
            'year' : str(date.year),
            'quarter' : self.string_utils.from_date_to_2_digit_quarter_string(date),
            'quarter_xbrl' : self.string_utils.from_date_to_1_digit_quarter_string(date),
            'month' : self.string_utils.from_date_to_2_digit_month_string(date),
        }

    def build_url(self, param):
        raise NotImplementedError

    def build_key(self, param):
        raise NotImplementedError
