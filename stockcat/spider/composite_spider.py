#-*- coding: utf-8 -*-

import datetime

class CompositeSpider():
    def __init__(self):
        self.ifrs_spider = None
        self.legacy_spider = None
        self.ifrs_date = datetime.date(2013, 1, 1)

    def crawl(self, param):
        if param['date'] >= self.ifrs_date:
            return self.ifrs_spider.crawl(param)
        else:
            return self.legacy_spider.crawl(param)

    def is_crawled(self, param):
        if param['date'] >= self.ifrs_date:
            return self.ifrs_spider.is_crawled(param)
        else:
            return self.legacy_spider.is_crawled(param)

    def get_crawled(self, param):
        if param['date'] >= self.ifrs_date:
            return self.ifrs_spider.get_crawled(param)
        else:
            return self.legacy_spider.get_crawled(param)
