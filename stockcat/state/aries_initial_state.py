#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class AriesInitialState(AriesState):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
    
    def run(self):
        self.logger.info('run [InitialState]')

    def next(self):
        self.logger.info('[InitialState] to [LoadState]')
        return self.state_machine.load_state