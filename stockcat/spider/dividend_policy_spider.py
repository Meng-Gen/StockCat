#-*- coding: utf-8 -*-

from stockcat.spider.spider import Spider

class DividendPolicySpider(Spider):
    def build_url(self, param):
        return '''http://jdata.yuanta.com.tw/z/zc/zcc/zcc_%s.djhtm''' \
                % (param['stock_symbol'])

    def build_key(self, param):
        return '''dividend_policy/%s'''\
                 % (param['stock_symbol'])