#-*- coding: utf-8 -*-

from stockcat.state.aries.state_machine import StateMachine
from stockcat.state.aries.entry_list_helper import EntryListHelper
from stockcat.spider.operating_revenue_summary_spider import OperatingRevenueSummarySpider
from stockcat.assembler.operating_revenue_summary_assembler import OperatingRevenueSummaryAssembler
from stockcat.feed.operating_revenue_feed import OperatingRevenueSummaryFeedBuilder

import datetime

class OperatingRevenueStateMachine(StateMachine):
    def __init__(self, memento_path='operating_revenue_memento.json'):
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
        entry_list = self.__get_entry_list()
        # !!! DEBUG ONLY !!!
        entry_list = entry_list[:2]
        return {
            'state' : 'spider',
            'all_entry_list' : list(entry_list),
            'todo_entry_list' : list(entry_list),
            'last_updated_date' : datetime.date(1949, 12, 7) 
        }

    def __get_entry_list(self):
        date_list = self.__get_date_list()
        market_type_list = self.__get_market_type_list()
        return self.helper.product(date_list, market_type_list)

    def __get_date_list(self):
        begin_date = datetime.date(2010, 6, 30)
        end_date = self.helper.get_now_date()
        return self.helper.get_date_list_by_month(begin_date, end_date)
        
    def __get_market_type_list(self):
        return self.helper.get_market_type_list()

