#-*- coding: utf-8 -*-

from stockcat.assembler.assemble_error import AssembleError
from stockcat.assembler.assemble_error import NoRecordAssembleError
from stockcat.assembler.assemble_error import OverQueryAssembleError
from stockcat.assembler.content_screener import ContentScreener
from stockcat.common.date_utils import DateUtils
from stockcat.database.database import Database

import random
import time

class AriesPipeline():
    def __init__(self):
        self.spider = None
        self.assembler = None
        self.feed_builder = None
        self.database = Database()
        self.date_utils = DateUtils()
        self.content_screener = ContentScreener()

    def run(self, stock_symbol, date, enable_list=['assembler', 'database']):
        try:
            param = self.__build_param(stock_symbol, date, enable_list)
            param = self.__run_spider(param)
            param = self.__run_assembler(param)
            param = self.__run_database(param)
        except OverQueryAssembleError as e:
            print e, 'We will force to run spider without over query error'
            param = self.__force_run_spider_without_over_query_error(param)
            param = self.__run_assembler(param)
            param = self.__run_database(param)
        except NoRecordAssembleError as e:
            print e, 'We will abort this pipeline'

    def run_many(self, stock_symbol, date_period, enable_list=['assembler', 'database']):
        begin_date, end_date = date_period
        for date in self.date_utils.range_date_by_quarter(begin_date, end_date):
            self.run(stock_symbol, date, enable_list)
            self.__avoid_blocking()
            
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
            feed = self.feed_builder.build(param['dao'])
            self.database.store(feed)
        return param

    def __force_run_spider_without_over_query_error(self, param):
        while True:
            self.spider.crawl(param['stock_symbol'], param['date'])
            content = self.spider.get_crawled(param['stock_symbol'], param['date'])
            try:
                self.content_screener.screen(content, param['stock_symbol'], param['date'])
            except OverQueryAssembleError:
                self.__avoid_blocking()
            except AssembleError:
                break
        return param

    def __avoid_blocking(self, a=3, b=5):
        time.sleep(random.randint(a, b))
