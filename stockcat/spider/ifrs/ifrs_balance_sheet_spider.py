#-*- coding: utf-8 -*-

from stockcat.spider.spider import Spider

class IfrsBalanceSheetSpider(Spider):
    def build_url(self, param):
        return '''http://mops.twse.com.tw/mops/web/ajax_t164sb03?encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=true&co_id=%s&year=%s&season=%s''' \
                % (param['stock_symbol'], param['roc_era'], param['quarter'])

    def build_key(self, param):
        return '''ifrs_balance_sheet/%s/%s/%s''' \
                % (param['stock_symbol'], param['year'], param['quarter'])
