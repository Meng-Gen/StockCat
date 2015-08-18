#-*- coding: utf-8 -*-

from stockcat.assembler.assemble_error import NoRecordAssembleError
from stockcat.common.date_utils import DateUtils
from stockcat.database.database import Database
from stockcat.feed.dividend_policy_feed import DividendPolicyFeed
from stockcat.spider.dividend_policy_spider import DividendPolicySpider
from stockcat.assembler.dividend_policy_assembler import DividendPolicyAssembler

import random
import time

class DividendPolicyPipeline():
    def __init__(self):
        self.spider = DividendPolicySpider()
        self.assembler = DividendPolicyAssembler()
        self.feed = DividendPolicyFeed()
        self.database = Database()
        self.date_utils = DateUtils()

    def run(self, stock_symbol, enable_list=['assembler', 'database']):
        try:
            param = self.__build_param(stock_symbol, enable_list)
            param = self.__run_spider(param)
            param = self.__run_assembler(param)
            param = self.__run_database(param)
        except NoRecordAssembleError as e:
            print e, '=> We will abort this pipeline'
            
    def __build_param(self, stock_symbol, enable_list):
        return { 'stock_symbol' : stock_symbol, 'enable_list' : enable_list, }

    def __run_spider(self, param):
        if 'spider' in param['enable_list']:
            self.spider.crawl(param['stock_symbol'])
        return param

    def __run_assembler(self, param):
        if 'assembler' in param['enable_list']:
            content = self.spider.get_crawled(param['stock_symbol'])
            param['dao'] = self.assembler.assemble(content, param['stock_symbol'])
        return param

    def __run_database(self, param):
        if 'database' in param['enable_list'] and 'dao' in param:
            feed = self.feed.get(param['dao'])
            self.database.store_dividend_policy(feed)
        return param

    def __avoid_blocking(self, a=3, b=5):
        time.sleep(random.randint(a, b))
