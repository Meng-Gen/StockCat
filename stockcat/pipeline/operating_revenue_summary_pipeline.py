#-*- coding: utf-8 -*-

from stockcat.common.date_utils import DateUtils
from stockcat.database.database import Database
from stockcat.feed.operating_revenue_summary_feed import OperatingRevenueSummaryFeed
from stockcat.spider.operating_revenue_summary_spider import OperatingRevenueSummarySpider
from stockcat.assembler.operating_revenue_summary_assembler import OperatingRevenueSummaryAssembler

import random
import time

class OperatingRevenueSummaryPipeline():
    def __init__(self):
        self.spider = OperatingRevenueSummarySpider()
        self.assembler = OperatingRevenueSummaryAssembler()
        self.feed = OperatingRevenueSummaryFeed()
        self.database = Database()
        self.date_utils = DateUtils()

    def run(self, date, enable_list=['assembler', 'database']):
        param = self.__build_param(date, enable_list)
        param = self.__run_spider(param)
        param = self.__run_assembler(param)
        param = self.__run_database(param)

    def run_many(self, date_period, enable_list=['assembler', 'database']):
        begin_date, end_date = date_period
        for date in self.date_utils.range_date_by_month(begin_date, end_date):
            self.run(stock_symbol, date, enable_list)
            self.__avoid_blocking()
            
    def __build_param(self, date, enable_list):
        return { 'date' : date, 'enable_list' : enable_list, }

    def __run_spider(self, param):
        if 'spider' in param['enable_list']:
            self.spider.crawl('stock_exchange_market', param['date'])
            self.__avoid_blocking()
            self.spider.crawl('otc_market', param['date'])
        return param

    def __run_assembler(self, param):
        if 'assembler' in param['enable_list']:
            content = self.spider.get_crawled('stock_exchange_market', param['date'])
            param['stock_exchange_market_dao'] = self.assembler.assemble(content, param['date'])
            content = self.spider.get_crawled('otc_market', param['date'])
            param['otc_market_dao'] = self.assembler.assemble(content, param['date'])
        return param

    def __run_database(self, param):
        if 'database' in param['enable_list']:
            if 'stock_exchange_market_dao' in param:
                feed = self.feed.get(param['stock_exchange_market_dao'])
                self.database.store_operating_revenue(feed)
            if 'otc_market_dao' in param:
                feed = self.feed.get(param['otc_market_dao'])
                self.database.store_operating_revenue(feed)
        return param

    def __avoid_blocking(self, a=3, b=5):
        time.sleep(random.randint(a, b))
