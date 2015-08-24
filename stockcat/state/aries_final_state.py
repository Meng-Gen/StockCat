#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class AriesFinalState(AriesState):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
    
    def next(self):
        raise NotImplementedError, 'we cannot move to next at final state'