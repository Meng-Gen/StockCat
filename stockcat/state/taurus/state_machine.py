#-*- coding: utf-8 -*-

from stockcat.database.database import Database

from stockcat.state.taurus.memento import Memento
from stockcat.state.aries_initial_state import AriesInitialState
from stockcat.state.aries_load_state import AriesLoadState
from stockcat.state.taurus.spider_state import SpiderState
from stockcat.state.taurus.assembler_state import AssemblerState
from stockcat.state.taurus.database_state import DatabaseState
from stockcat.state.aries_final_state import AriesFinalState

import logging

class TaurusStateMachine():
    def __init__(self, memento_path, spider, assembler, feed_builder):
        self.logger = logging.getLogger(__name__)
        
        # memento for state machine
        self.memento = Memento(memento_path)

        # prepare spider, assembler, feed builder, database
        self.spider = spider
        self.assembler = assembler
        self.feed_builder = feed_builder
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
