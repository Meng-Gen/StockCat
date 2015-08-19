#-*- coding: utf-8 -*-

from stockcat.spider.taurus_spider import TaurusSpider
from stockcat.spider.ifrs.ifrs_operating_revenue_spider import IfrsOperatingRevenueSpider
from stockcat.spider.legacy.legacy_operating_revenue_spider import LegacyOperatingRevenueSpider

class OperatingRevenueSpider(TaurusSpider):
    def __init__(self):
        self.ifrs_spider = IfrsOperatingRevenueSpider()
        self.legacy_spider = LegacyOperatingRevenueSpider()
