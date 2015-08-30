#-*- coding: utf-8 -*-

from stockcat.spider.composite_spider import CompositeSpider
from stockcat.spider.ifrs.ifrs_operating_revenue_spider import IfrsOperatingRevenueSpider
from stockcat.spider.legacy.legacy_operating_revenue_spider import LegacyOperatingRevenueSpider

class OperatingRevenueSpider(CompositeSpider):
    def __init__(self):
        CompositeSpider.__init__(self)
        self.ifrs_spider = IfrsOperatingRevenueSpider()
        self.legacy_spider = LegacyOperatingRevenueSpider()
