#-*- coding: utf-8 -*-

from stockcat.common.date_utils import DateUtils
from stockcat.pipeline.operating_revenue_summary_pipeline import OperatingRevenueSummaryPipeline
from stockcat.pipeline.stock_symbol_pipeline import StockSymbolPipeline

import datetime

class Initializer():
    def __init__(self):
        self.date_utils = DateUtils()
        self.now_date = self.date_utils.now_date()

    def init_stock_symbol(self):
        stage_list = ['spider', 'assembler', 'database']
        StockSymbolPipeline().run(stage_list)

    def init_operating_revenue_summary(self):
        date_period = datetime.date(2010, 6, 30), self.now_date
        stage_list = ['spider', 'assembler', 'database']
        OperatingRevenueSummaryPipeline().run_many(date_period, stage_list)
