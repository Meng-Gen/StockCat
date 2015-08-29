#-*- coding: utf-8 -*-

from stockcat.pipeline.state.state_machine import StateMachine
from stockcat.pipeline.state.entry_list_helper import EntryListHelper
from stockcat.spider.operating_revenue_summary_spider import OperatingRevenueSummarySpider
from stockcat.assembler.operating_revenue_summary_assembler import OperatingRevenueSummaryAssembler
from stockcat.feed.operating_revenue_feed import OperatingRevenueSummaryFeedBuilder

import datetime

class OperatingRevenuePipeline(StateMachine):
    def __init__(self, memento_path='./stockcat/data/memento/operating_revenue.json'):
        self.helper = EntryListHelper()
        memento_param = {
            'path' : memento_path, 
            'default_value' : self.__get_default_value(),
            'filter_key_list' : [ 'state', 'all_entry_list', 'todo_entry_list', 'last_updated_date' ],
        }
        param = {
            'memento' : memento_param,
            'spider' : OperatingRevenueSummarySpider(), 
            'assembler' : OperatingRevenueSummaryAssembler(), 
            'feed_builder' : OperatingRevenueSummaryFeedBuilder(),
        }
        StateMachine.__init__(self, param)

    def __get_default_value(self):
        entry_list = self.helper.get_operating_revenue_entry_list()
        # !!! DEBUG ONLY !!!
        entry_list = entry_list[:2]
        return {
            'state' : 'spider',
            'all_entry_list' : list(entry_list),
            'todo_entry_list' : list(entry_list),
            'last_updated_date' : datetime.date(1949, 12, 7) 
        }
