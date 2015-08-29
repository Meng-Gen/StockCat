#-*- coding: utf-8 -*-

from stockcat.pipeline.state.state import State

import logging

class FinalState(State):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
    
    def next(self):
        raise NotImplementedError, 'we cannot move to next at final state'