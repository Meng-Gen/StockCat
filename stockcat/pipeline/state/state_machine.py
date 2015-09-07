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
        self.memento.load()

        # prepare database
        self.spider = param['spider']
        self.assembler = param['assembler']
        self.feed_builder = param['feed_builder']
        self.database = Database()

        # all states are listed here
        self.state_map = {
            'InitialState' : InitialState(self),
            'LoadState' : LoadState(self),
            'SpiderState' : SpiderState(self),
            'AssemblerState' : AssemblerState(self),
            'DatabaseState' : DatabaseState(self),
            'FinalState' : FinalState(self),
        }

        # set transition table
        self.transition_table = param['transition_table'] 

        # set current state
        self.curr_state = 'InitialState'

    def run(self):
        while self.curr_state != 'FinalState':
            try:
                self.state_map[self.curr_state].run()
                self.curr_state = self.next() 
            except KeyboardInterrupt:
                self.state_map[self.curr_state].tear_down()
                raise

    def next(self):
        transition_value = self.get_value('transition_value', '')
        for entry in self.transition_table:
            state, next_state, expected_value = entry
            if (self.curr_state, transition_value) == (state, expected_value):
                return next_state
        self.logger.error('transition table is not completed')
        return 'FinalState'

    def get_value(self, key, default_value=None):
        memento_value = self.memento.get_value()
        if key in memento_value:
            return memento_value[key]
        else:
            return default_value

    def set_value(self, key, value):
        memento_value = self.memento.get_value()
        memento_value[key] = value

    def save_memento(self):
        self.memento.save()
