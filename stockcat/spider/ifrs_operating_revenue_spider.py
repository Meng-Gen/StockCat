#-*- coding: utf-8 -*-

from stockcat.spider.spider_storage import SpiderStorage
from stockcat.common.string_utils import StringUtils

class IfrsOperatingRevenueSpider():
    def __init__(self):
        self.storage = SpiderStorage()
        self.string_utils = StringUtils()
        
    def crawl(self, stock_symbol, date):
        params = self.__parse_params(stock_symbol, date)
        url = self.__build_url(params)
        key = self.__build_key(params)
        self.storage.set(key, url)

    def is_crawled(self, stock_symbol, date):
        params = self.__parse_params(stock_symbol, date)
        key = self.__build_key(params)
        return self.storage.contains(key)

    def __parse_params(self, stock_symbol, date):
        return {
            'stock_symbol' : stock_symbol,
            'roc_era' : self.string_utils.from_date_to_roc_era_string(date),
            'year' : str(date.year),
            'month' : self.string_utils.from_date_to_2_digit_month_string(date),
        }

    def __build_url(self, params):
        # do not forget escape %
        return '''http://mops.twse.com.tw/mops/web/ajax_t05st10_ifrs?encodeURIComponent=1&run=Y&step=0&colorchg=&TYPEK=sii%%20&co_id=%s&off=1&year=%s&month=%s&firstin=true''' \
                % (params['stock_symbol'], params['roc_era'], params['month'])

    def __build_key(self, params):
        return '''ifrs_operating_revenue/%s/%s/%s''' \
                % (params['stock_symbol'], params['year'], params['month'])
