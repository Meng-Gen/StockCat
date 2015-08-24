#-*- coding: utf-8 -*-

from stockcat.spider.stock_symbol_spider import StockSymbolSpider
from stockcat.assembler.stock_symbol_assembler import StockSymbolAssembler
from stockcat.feed.stock_symbol_feed import StockSymbolFeedBuilder
from stockcat.database.database import Database

from stockcat.state.stock_symbol.memento import Memento
from stockcat.state.aries_initial_state import AriesInitialState
from stockcat.state.aries_load_state import AriesLoadState
from stockcat.state.stock_symbol.spider_state import SpiderState
from stockcat.state.stock_symbol.assembler_state import AssemblerState
from stockcat.state.stock_symbol.database_state import DatabaseState
from stockcat.state.aries_final_state import AriesFinalState

import logging

class StateMachine():
    def __init__(self, memento_path='stock_symbol_memento.json'):
        self.logger = logging.getLogger(__name__)
        
        # memento for state machine
        self.memento = Memento(memento_path)

        # prepare spider, assembler, feed builder, database
        spider = StockSymbolSpider()
        assembler = StockSymbolAssembler()
        feed_builder = StockSymbolFeedBuilder()
        database = Database()

        # all states are listed here
        self.initial_state = AriesInitialState(self)
        self.load_state = AriesLoadState(self)
        self.spider_state = SpiderState(self, spider)
        self.assembler_state = AssemblerState(self, spider, assembler)
        self.database_state = DatabaseState(self, feed_builder, database)
        self.final_state = AriesFinalState(self)

        # current state
        self.curr_state = self.initial_state

    def run(self):
        while self.curr_state != self.final_state:
            self.curr_state.run()
            self.curr_state = self.curr_state.next()
