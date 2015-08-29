#-*- coding: utf-8 -*-

from stockcat.database.database import Database
from stockcat.pipeline.state.memento import Memento
from stockcat.pipeline.state.initial_state import InitialState
from stockcat.pipeline.state.load_state import LoadState
from stockcat.pipeline.state.spider_state import SpiderState
from stockcat.pipeline.state.assembler_state import AssemblerState
from stockcat.pipeline.state.database_state import DatabaseState
from stockcat.pipeline.state.final_state import FinalState

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
            try:
                self.curr_state.run()
                self.curr_state = self.curr_state.next()
            except KeyboardInterrupt:
                self.curr_state.tear_down()
                raise
