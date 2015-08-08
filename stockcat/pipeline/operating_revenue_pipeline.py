#-*- coding: utf-8 -*-

from stockcat.spider.operating_revenue_spider import OperatingRevenueSpider
from stockcat.assembler.operating_revenue_assembler import OperatingRevenueAssembler
from stockcat.database.database import Database

class OperatingRevenuePipeline():
    def __init__(self):
        self.spider = OperatingRevenueSpider()
        self.assembler = OperatingRevenueAssembler()
        self.database = Database()

    def run(self, stock_symbol, date, enable_list=['assembler', 'database']):
        if 'spider' in enable_list:
            self.spider.crawl(stock_symbol, date)

        dao = None
        if 'assembler' in enable_list:
            content = self.spider.get_crawled(stock_symbol, date)
            dao = self.assembler.assemble(content, stock_symbol, date)

        if 'database' in enable_list:
            self.database.insert_operating_revenue(dao)

        return True