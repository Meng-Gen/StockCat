#-*- coding: utf-8 -*-

from stockcat.dao.operating_revenue_dao import OperatingRevenueDao

class OperatingRevenuePipeline():
    def run(self, stock_symbol):
        print stock_symbol