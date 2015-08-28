#-*- coding: utf-8 -*-

from stockcat.spider.storage.spider_storage import SpiderStorage
from stockcat.common.string_utils import StringUtils

class OperatingRevenueSummarySpider():
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
        market_type = param['market_type']
        date = param['date']
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

    def build_url(self, param):
        return '''http://mops.twse.com.tw/nas/t21/%s/t21sc03_%s_%s.html''' \
                % (param['market_code'], param['roc_era'], param['month'])

    def build_key(self, param):
        return '''operating_revenue_summary/%s/%s/%s''' \
                % (param['market_type'], param['year'], param['month'])