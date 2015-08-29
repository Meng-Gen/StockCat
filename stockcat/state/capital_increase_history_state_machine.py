#-*- coding: utf-8 -*-

from stockcat.state.aries.state_machine import StateMachine
from stockcat.state.aries.entry_list_helper import EntryListHelper
from stockcat.spider.capital_increase_history_spider import CapitalIncreaseHistorySpider
from stockcat.assembler.capital_increase_history_assembler import CapitalIncreaseHistoryAssembler
from stockcat.feed.capital_increase_history_feed import CapitalIncreaseHistoryFeedBuilder

import datetime

class CapitalIncreaseHistoryStateMachine(StateMachine):
    def __init__(self, memento_path='capital_increase_history_memento.json'):
        memento_param = {
            'path' : memento_path, 
            'default_value' : self.__get_default_value(),
            'filter_key_list' : [ 'state', 'all_entry_list', 'todo_entry_list', 'last_updated_date' ],
        }
        param = {
            'memento' : memento_param,
            'spider' : CapitalIncreaseHistorySpider(), 
            'assembler' : CapitalIncreaseHistoryAssembler(), 
            'feed_builder' : CapitalIncreaseHistoryFeedBuilder(),
        }
        StateMachine.__init__(self, param)

    def __get_default_value(self):
        stock_symbol_list = EntryListHelper().get_stock_symbol_list()
        # !!! DEBUG ONLY !!!
        stock_symbol_list = stock_symbol_list[:1]
        return {
            'state' : 'spider',
            'all_entry_list' : list(stock_symbol_list),
            'todo_entry_list' : list(stock_symbol_list),
            'last_updated_date' : datetime.date(1949, 12, 7) 
        }
