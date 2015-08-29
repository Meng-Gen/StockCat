#-*- coding: utf-8 -*-

from stockcat.pipeline.state.state import State

import logging

class InitialState(State):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
    
    def run(self):
        self.logger.info('run initial state')

    def next(self):
        self.logger.info('move initial state to load state')
        return self.state_machine.load_state