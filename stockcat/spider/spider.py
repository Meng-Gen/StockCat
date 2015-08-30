#-*- coding: utf-8 -*-

from stockcat.spider.storage.spider_storage import SpiderStorage
from stockcat.common.string_utils import StringUtils

class Spider():
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
        output = {}
        if 'stock_symbol' in param:
            output['stock_symbol'] = param['stock_symbol']
        if 'date' in param:
            date = param['date']
            output['roc_era'] = self.string_utils.from_date_to_roc_era_string(date)
            output['year'] = str(date.year)
            output['quarter'] = self.string_utils.from_date_to_2_digit_quarter_string(date)
            output['quarter_xbrl'] = self.string_utils.from_date_to_1_digit_quarter_string(date)
            output['month'] = self.string_utils.from_date_to_2_digit_month_string(date)
        if 'market_type' in param:
            market_type = param['market_type']
            output['market_type'] = market_type
            output['market_code'] = self.__extend_market_code(market_type)
            output['market_mode'] = self.__extend_market_mode(market_type)
        return output

    def __extend_market_code(self, market_type):
        code_map = {
            'stock_exchange_market' : 'sii',
            'otc_market' : 'otc',
        }
        return code_map[market_type]

    def __extend_market_mode(self, market_type):
        mode_map = {
            'stock_exchange_market' : '2',
            'otc_market' : '4',
        }
        return mode_map[market_type]

    def build_url(self, param):
        raise NotImplementedError

    def build_key(self, param):
        raise NotImplementedError
