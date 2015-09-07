#-*- coding: utf-8 -*-

from stockcat.pipeline.state.state import State

import logging

class LoadState(State):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine

    def run(self):
        self.logger.info('run load state')
        state = self.state_machine.get_value('state')
        self.state_machine.set_value('transition_value', state)
