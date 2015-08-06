#-*- coding: utf-8 -*-

from stockcat.spider.single_stock_spider import SingleStockSpider

class IfrsOperatingRevenueSpider(SingleStockSpider):
    def build_url(self, params):
        # do not forget escape %
        return '''http://mops.twse.com.tw/mops/web/ajax_t05st10_ifrs?encodeURIComponent=1&run=Y&step=0&colorchg=&TYPEK=sii%%20&co_id=%s&off=1&year=%s&month=%s&firstin=true''' \
                % (params['stock_symbol'], params['roc_era'], params['month'])

    def build_key(self, params):
        return '''ifrs_operating_revenue/%s/%s/%s''' \
                % (params['stock_symbol'], params['year'], params['month'])
