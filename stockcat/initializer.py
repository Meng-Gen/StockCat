#-*- coding: utf-8 -*-

from stockcat.analyzer.stock_symbol_analyzer import StockSymbolAnalyzer
from stockcat.common.date_utils import DateUtils
from stockcat.pipeline.operating_revenue_summary_pipeline import OperatingRevenueSummaryPipeline
from stockcat.pipeline.stock_symbol_pipeline import StockSymbolPipeline

import datetime
import logging

class Initializer():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.date_utils = DateUtils()
        self.now_date = self.date_utils.now_date()
        self.stock_symbol_list = None

    def init_stock_symbol(self):
        self.logger.info('initialize stock symbol')
        stage_list = ['spider', 'assembler', 'database']
        StockSymbolPipeline().run(stage_list)

    def init_operating_revenue_summary(self):
        self.logger.info('initialize operating revenue summary')
        date_period = datetime.date(2010, 6, 30), self.now_date
        stage_list = ['spider', 'assembler', 'database']
        OperatingRevenueSummaryPipeline().run_many(date_period, stage_list)

    def init_dividend_policy(self):
        self.logger.info('initialize dividend policy')
        stock_symbol_list = self.__get_stock_symbol_list()
        self.logger.info('need to initialize {0} stock symbols'.format(len(stock_symbol_list)))

    def __get_stock_symbol_list(self):
        if not self.stock_symbol_list:
            analyzer = StockSymbolAnalyzer()
            self.stock_symbol_list = analyzer.get_stock_symbol_list()
            self.logger.debug(self.stock_symbol_list)
        return self.stock_symbol_list
