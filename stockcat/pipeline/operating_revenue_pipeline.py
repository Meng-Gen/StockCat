#-*- coding: utf-8 -*-

from stockcat.database.database import Database
from stockcat.feed.operating_revenue_feed import OperatingRevenueFeed
from stockcat.spider.operating_revenue_spider import OperatingRevenueSpider
from stockcat.assembler.operating_revenue_assembler import OperatingRevenueAssembler

class OperatingRevenuePipeline():
    def __init__(self):
        self.spider = OperatingRevenueSpider()
        self.assembler = OperatingRevenueAssembler()
        self.feed = OperatingRevenueFeed()
        self.database = Database()

    def run(self, stock_symbol, date, enable_list=['assembler', 'database']):
        param = self.__build_param(stock_symbol, date, enable_list)
        param = self.__run_spider(param)
        param = self.__run_assembler(param)
        param = self.__run_database(param)

    def __build_param(self, stock_symbol, date, enable_list):
        return { 'stock_symbol' : stock_symbol, 'date' : date, 'enable_list' : enable_list, }

    def __run_spider(self, param):
        if 'spider' in param['enable_list']:
            self.spider.crawl(param['stock_symbol'], param['date'])
        return param

    def __run_assembler(self, param):
        if 'assembler' in param['enable_list']:
            content = self.spider.get_crawled(param['stock_symbol'], param['date'])
            param['dao'] = self.assembler.assemble(content, param['stock_symbol'], param['date'])
        return param

    def __run_database(self, param):
        if 'database' in param['enable_list'] and 'dao' in param:
            feed = self.feed.get(param['dao'])
            self.database.store_operating_revenue(feed)
        return param
