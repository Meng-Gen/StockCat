#-*- coding: utf-8 -*-

from stockcat.spider.aries_spider import AriesSpider

class LegacyCashFlowSpider(AriesSpider):
    def build_url(self, params):
        return '''http://mops.twse.com.tw/mops/web/ajax_t05st39?encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=false&co_id=%s&year=%s&season=%s''' \
                % (params['stock_symbol'], params['roc_era'], params['quarter'])

    def build_key(self, params):
        return '''legacy_cash_flow/%s/%s/%s''' \
                % (params['stock_symbol'], params['year'], params['quarter'])