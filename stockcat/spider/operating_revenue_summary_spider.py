#-*- coding: utf-8 -*-

from stockcat.spider.spider_storage import SpiderStorage
from stockcat.common.string_utils import StringUtils

class OperatingRevenueSummarySpider():
    def __init__(self):
        self.storage = SpiderStorage()
        self.string_utils = StringUtils()

    def crawl(self, market_type, date):
        params = self.__parse_params(market_type, date)
        url = self.__build_url(params)
        key = self.__build_key(params)
        self.storage.set(key, url)
        
    def is_crawled(self, market_type, date):
        params = self.__parse_params(market_type, date)
        key = self.__build_key(params)
        return self.storage.contains(key)

    def get_crawled(self, market_type, date):
        params = self.__parse_params(market_type, date)
        key = self.__build_key(params)
        return self.storage.get(key)
        
    def __parse_params(self, market_type, date):
        return {
            'market_type' : market_type,
            'market_code' : self.__parse_market_code(market_type),
            'roc_era' : self.string_utils.from_date_to_roc_era_string(date),
            'year' : str(date.year),
            'month' : str(date.month), 
        }

    def __parse_market_code(self, market_type):
        if market_type == 'stock_exchange_market':
            return 'sii'
        elif market_type == 'otc_market':
            return 'otc'
        else:
            raise ValueError

    def __build_url(self, params):
        return '''http://mops.twse.com.tw/nas/t21/%s/t21sc03_%s_%s.html''' \
                % (params['market_code'], params['roc_era'], params['month'])

    def __build_key(self, params):
        return '''operating_revenue_summary/%s/%s/%s''' \
                % (params['market_type'], params['year'], params['month'])