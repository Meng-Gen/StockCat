#-*- coding: utf-8 -*-

from stockcat.database.database import Database
from stockcat.state.aries.memento import Memento
from stockcat.state.aries.initial_state import InitialState
from stockcat.state.aries.load_state import LoadState
from stockcat.state.aries.spider_state import SpiderState
from stockcat.state.aries.assembler_state import AssemblerState
from stockcat.state.aries.database_state import DatabaseState
from stockcat.state.aries.final_state import FinalState

import logging

class StateMachine():
    def __init__(self, param):
        self.logger = logging.getLogger(__name__)

        # memento for state machine
        self.memento = Memento(param['memento'])

        # prepare database
        self.spider = param['spider']
        self.assembler = param['assembler']
        self.feed_builder = param['feed_builder']
        self.database = Database()

        # all states are listed here
        self.initial_state = InitialState(self)
        self.load_state = LoadState(self)
        self.spider_state = SpiderState(self)
        self.assembler_state = AssemblerState(self)
        self.database_state = DatabaseState(self)
        self.final_state = FinalState(self)

        # current state
        self.curr_state = self.initial_state

    def run(self):
        while self.curr_state != self.final_state:
            self.curr_state.run()
            self.curr_state = self.curr_state.next()
