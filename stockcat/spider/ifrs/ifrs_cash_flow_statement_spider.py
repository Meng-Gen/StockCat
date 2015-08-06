#-*- coding: utf-8 -*-

from stockcat.spider.single_stock_spider import SingleStockSpider

class IfrsCashFlowStatementSpider(SingleStockSpider):
    def build_url(self, params):
        return '''http://mops.twse.com.tw/mops/web/ajax_t164sb05?encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=true&co_id=%s&year=%s&season=%s''' \
                % (params['stock_symbol'], params['roc_era'], params['season'])

    def build_key(self, params):
        return '''ifrs_cash_flow_statement/%s/%s/%s''' \
                % (params['stock_symbol'], params['year'], params['season'])