#-*- coding: utf-8 -*-

from stockcat.spider.aries_spider import AriesSpider

class LegacyOperatingRevenueSpider(AriesSpider):
    def build_url(self, param):
        # do not forget escape %
        return '''http://mops.twse.com.tw/mops/web/ajax_t05st10?encodeURIComponent=1&run=Y&step=0&colorchg=&TYPEK=sii%%20&co_id=%s&off=1&year=%s&month=%s&firstin=true''' \
                % (param['stock_symbol'], param['roc_era'], param['month'])

    def build_key(self, param):
        return '''legacy_operating_revenue/%s/%s/%s''' \
                % (param['stock_symbol'], param['year'], param['month'])
