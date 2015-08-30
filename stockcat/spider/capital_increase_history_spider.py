#-*- coding: utf-8 -*-

from stockcat.spider.spider import Spider

class CapitalIncreaseHistorySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zcb/zcb_%s.djhtm''' \
                % (param['stock_symbol'])

    def build_key(self, param):
        return '''capital_increase_history/%s''' \
                % (param['stock_symbol'])