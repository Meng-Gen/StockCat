#-*- coding: utf-8 -*-

from stockcat.spider.spider import Spider

class OperatingRevenueSummarySpider(Spider):
    def build_url(self, param):
        return '''http://mops.twse.com.tw/nas/t21/%s/t21sc03_%s_%s.html''' \
                % (param['market_code'], param['roc_era'], param['month'])

    def build_key(self, param):
        return '''operating_revenue_summary/%s/%s/%s''' \
                % (param['market_type'], param['year'], param['month'])
