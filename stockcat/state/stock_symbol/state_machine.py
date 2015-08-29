#-*- coding: utf-8 -*-

from stockcat.spider.stock_symbol_spider import StockSymbolSpider
from stockcat.assembler.stock_symbol_assembler import StockSymbolAssembler
from stockcat.feed.stock_symbol_feed import StockSymbolFeedBuilder
from stockcat.database.database import Database

from stockcat.state.aries_memento import AriesMemento
from stockcat.state.aries_initial_state import AriesInitialState
from stockcat.state.aries_load_state import AriesLoadState
from stockcat.state.stock_symbol.spider_state import SpiderState
from stockcat.state.stock_symbol.assembler_state import AssemblerState
from stockcat.state.stock_symbol.database_state import DatabaseState
from stockcat.state.aries_final_state import AriesFinalState

import datetime
import logging

class StateMachine():
    def __init__(self, memento_path='stock_symbol_memento.json'):
        self.logger = logging.getLogger(__name__)
        
        # memento for state machine
        self.memento = self.__build_memento(memento_path)

        # prepare spider, assembler, feed builder, database
        self.spider = StockSymbolSpider()
        self.assembler = StockSymbolAssembler()
        self.feed_builder = StockSymbolFeedBuilder()
        self.database = Database()

        # all states are listed here
        self.initial_state = AriesInitialState(self)
        self.load_state = AriesLoadState(self)
        self.spider_state = SpiderState(self)
        self.assembler_state = AssemblerState(self)
        self.database_state = DatabaseState(self)
        self.final_state = AriesFinalState(self)

        # current state
        self.curr_state = self.initial_state

    def run(self):
        while self.curr_state != self.final_state:
            self.curr_state.run()
            self.curr_state = self.curr_state.next()

    def __build_memento(self, path):
        param = {
            'path' : path,
            'default_value' : self.__get_default_value(),
            'filter_key_list' : [ 'state', 'all_entry_list', 'todo_entry_list', 'last_updated_date' ]
        }
        return AriesMemento(param)

    def __get_default_value(self):
        return {
            'state' : 'spider',
            'all_entry_list' : [
                { 'market_type' : 'stock_exchange_market' },
                { 'market_type' : 'otc_market' },
            ],
            'todo_entry_list' : [
                { 'market_type' : 'stock_exchange_market' },
                { 'market_type' : 'otc_market' },
            ],            
            'last_updated_date' : datetime.date(1949, 12, 7) 
        }
