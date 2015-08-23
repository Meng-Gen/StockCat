#-*- coding: utf-8 -*-

from stockcat.assembler.assemble_error import NoRecordAssembleError
from stockcat.common.date_utils import DateUtils
from stockcat.database.database import Database
from stockcat.spider.operating_revenue_summary_spider import OperatingRevenueSummarySpider
from stockcat.assembler.operating_revenue_summary_assembler import OperatingRevenueSummaryAssembler
from stockcat.feed.operating_revenue_feed import OperatingRevenueSummaryFeedBuilder

import logging
import random
import time

class OperatingRevenueSummaryPipeline():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.spider = OperatingRevenueSummarySpider()
        self.assembler = OperatingRevenueSummaryAssembler()
        self.feed_builder = OperatingRevenueSummaryFeedBuilder()
        self.database = Database()
        self.date_utils = DateUtils()

    def run(self, date, enable_list=['assembler', 'database']):
        try:
            param = self.__build_param(date, enable_list)
            param = self.__run_spider(param)
            param = self.__run_assembler(param)
            param = self.__run_database(param)
        except NoRecordAssembleError as e:
            print e, '=> We will abort this pipeline'

    def run_many(self, date_period, enable_list=['assembler', 'database']):
        begin_date, end_date = date_period
        for date in self.date_utils.range_date_by_month(begin_date, end_date):
            self.run(date, enable_list)
            
    def __build_param(self, date, enable_list):
        return { 'date' : date, 'enable_list' : enable_list, }

    def __run_spider(self, param):
        if 'spider' in param['enable_list']:
            self.logger.info('crawl stock exchange market operating revenue summary: {0}'.format(param['date']))
            self.spider.crawl('stock_exchange_market', param['date'])
            
            self.__avoid_blocking()
            
            self.logger.info('crawl otc market operating revenue summary: {0}'.format(param['date']))
            self.spider.crawl('otc_market', param['date'])
        return param

    def __run_assembler(self, param):
        if 'assembler' in param['enable_list']:
            self.logger.info('assemble stock exchange market operating revenue summary: {0}'.format(param['date']))
            content = self.spider.get_crawled('stock_exchange_market', param['date'])
            param['stock_exchange_market_dao'] = self.assembler.assemble(content, param['date'])
            
            self.logger.info('assemble otc market operating revenue summary: {0}'.format(param['date']))
            content = self.spider.get_crawled('otc_market', param['date'])
            param['otc_market_dao'] = self.assembler.assemble(content, param['date'])
        return param

    def __run_database(self, param):
        if 'database' in param['enable_list']:
            if 'stock_exchange_market_dao' in param:
                self.logger.info('store stock exchange market operating revenue summary: {0}'.format(param['date']))
                feed = self.feed_builder.build(param['stock_exchange_market_dao'])
                self.database.store(feed)                
            
            if 'otc_market_dao' in param:
                self.logger.info('store otc market operating revenue summary: {0}'.format(param['date']))
                feed = self.feed_builder.build(param['otc_market_dao'])
                self.database.store(feed)                
        return param

    def __avoid_blocking(self, a=3, b=5):
        time.sleep(random.randint(a, b))
