#-*- coding: utf-8 -*-

from stockcat.state.aries.state_machine import StateMachine
from stockcat.state.aries.entry_list_helper import EntryListHelper
from stockcat.spider.stock_symbol_spider import StockSymbolSpider
from stockcat.assembler.stock_symbol_assembler import StockSymbolAssembler
from stockcat.feed.stock_symbol_feed import StockSymbolFeedBuilder

import datetime

class StockSymbolStateMachine(StateMachine):
    def __init__(self, memento_path='stock_symbol_memento.json'):
        memento_param = {
            'path' : memento_path, 
            'default_value' : self.__get_default_value(),
            'filter_key_list' : [ 'state', 'all_entry_list', 'todo_entry_list', 'last_updated_date' ],
        }
        param = {
            'memento' : memento_param,
            'spider' : StockSymbolSpider(), 
            'assembler' : StockSymbolAssembler(), 
            'feed_builder' : StockSymbolFeedBuilder(),
        }
        StateMachine.__init__(self, param)

    def __get_default_value(self):
        entry_list = EntryListHelper().get_market_type_list()
        return {
            'state' : 'spider',
            'all_entry_list' : list(entry_list),
            'todo_entry_list' : list(entry_list),
            'last_updated_date' : datetime.date(1949, 12, 7) 
        }
