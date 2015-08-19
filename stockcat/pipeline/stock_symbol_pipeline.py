#-*- coding: utf-8 -*-

from stockcat.assembler.assemble_error import NoRecordAssembleError
from stockcat.assembler.stock_symbol_assembler import StockSymbolAssembler
from stockcat.database.database import Database
from stockcat.feed.stock_symbol_feed import StockSymbolFeedBuilder
from stockcat.spider.stock_symbol_spider import StockSymbolSpider

import random
import time

class StockSymbolPipeline():
    def __init__(self):
        self.spider = StockSymbolSpider()
        self.assembler = StockSymbolAssembler()
        self.feed_builder = StockSymbolFeedBuilder()
        self.database = Database()

    def run(self, enable_list=['assembler', 'database']):
        param = self.__build_param(enable_list)
        param = self.__run_spider(param)
        param = self.__run_assembler(param)
        param = self.__run_database(param)
            
    def __build_param(self, enable_list):
        return { 'enable_list' : enable_list, }

    def __run_spider(self, param):
        if 'spider' in param['enable_list']:
            self.spider.crawl('stock_exchange_market')
            self.__avoid_blocking()
            self.spider.crawl('otc_market')
        return param

    def __run_assembler(self, param):
        if 'assembler' in param['enable_list']:
            param['stock_exchange_market_dao'] = self.assembler.assemble(self.spider.get_crawled('stock_exchange_market'))
            param['otc_market_dao'] = self.assembler.assemble(self.spider.get_crawled('otc_market'))
        return param

    def __run_database(self, param):
        if 'database' in param['enable_list']:
            if 'stock_exchange_market_dao' in param:
                feed = self.feed_builder.build(param['stock_exchange_market_dao'])
                self.database.store(feed)
            if 'otc_market_dao' in param:
                feed = self.feed_builder.build(param['otc_market_dao'])
                self.database.store(feed)
        return param

    def __avoid_blocking(self, a=3, b=5):
        time.sleep(random.randint(a, b))
