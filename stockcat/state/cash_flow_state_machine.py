#-*- coding: utf-8 -*-

from stockcat.state.aries.state_machine import StateMachine
from stockcat.state.aries.entry_list_helper import EntryListHelper
from stockcat.spider.cash_flow_spider import CashFlowSpider
from stockcat.assembler.cash_flow_assembler import CashFlowAssembler
from stockcat.feed.cash_flow_feed import CashFlowFeedBuilder

import datetime

class CashFlowStateMachine(StateMachine):
    def __init__(self, memento_path='cash_flow_memento.json'):
        self.helper = EntryListHelper()
        memento_param = {
            'path' : memento_path, 
            'default_value' : self.__get_default_value(),
            'filter_key_list' : [ 'state', 'all_entry_list', 'todo_entry_list', 'last_updated_date' ],
        }
        param = {
            'memento' : memento_param,
            'spider' : CashFlowSpider(), 
            'assembler' : CashFlowAssembler(), 
            'feed_builder' : CashFlowFeedBuilder(),
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
        entry_list = []
        site_begin_date = datetime.date(1996, 3, 31)
        # !!! DEBUG ONLY !!!
        site_begin_date = datetime.date(2014, 3, 31)
        end_date = self.helper.get_now_date()
        for stock_symbol in self.helper.get_stock_symbol_list():
            begin_date = max(site_begin_date, stock_symbol['listing_date'])
            for date in self.helper.get_date_list_by_quarter(begin_date, end_date):
                entry = {
                    'stock_symbol' : stock_symbol['stock_symbol'],
                    'date' : date['date'],
                }
                entry_list.append(entry)
        return entry_list
