#-*- coding: utf-8 -*-

from stockcat.spider.spider import Spider

class IfrsOperatingRevenueSpider(Spider):
    def build_url(self, param):
        # do not forget escape %
        return '''http://mops.twse.com.tw/mops/web/ajax_t05st10_ifrs?encodeURIComponent=1&run=Y&step=0&colorchg=&TYPEK=sii%%20&co_id=%s&off=1&year=%s&month=%s&firstin=true''' \
                % (param['stock_symbol'], param['roc_era'], param['month'])

    def build_key(self, param):
        return '''ifrs_operating_revenue/%s/%s/%s''' \
                % (param['stock_symbol'], param['year'], param['month'])
