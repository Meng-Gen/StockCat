#-*- coding: utf-8 -*-

from stockcat.common.file_utils import FileUtils

import datetime

class StockSymbolFeed():
    def __init__(self):
        self.url = self.__build_url()
        self.filepath = self.__build_filepath()

    def get(self):
        self.__copy_url_to_file()
        #self.__assemble()

    def __copy_url_to_file(self):
        file_utils = FileUtils()
        for market_type in self.url:
            file_utils.copy_url_to_file(self.url[market_type], self.filepath[market_type])

    def __build_url(self):
        return {
            # 上市股號
            "stock_exchange_market" : 
            "http://isin.twse.com.tw/isin/C_public.jsp?strMode=2", 

            # 上櫃股號
            "otc_market" : 
            "http://isin.twse.com.tw/isin/C_public.jsp?strMode=4", 
        }

    def __build_filepath(self):
        return {
            # 上市股號
            "stock_exchange_market" : 
            "./stockcat/data/stock_symbol/stock_exchange_market.html",

            # 上櫃股號
            "otc_market" : 
            "./stockcat/data/stock_symbol/otc_market.html",
        }
