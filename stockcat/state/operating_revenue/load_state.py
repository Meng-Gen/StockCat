#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class LoadState(AriesState):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine

    def run(self):
        self.logger.info('run [LoadState]')
        self.state_machine.memento.load()

    def next(self):
        value = self.state_machine.memento.get_value()
        state = value['state']
        if state in ['spider']:
            self.logger.info('[LoadState] to [SpiderState]')
            return self.state_machine.spider_state
        elif state in ['assembler', 'database']:
            self.logger.info('[LoadState] to [AssemblerState]')
            return self.state_machine.assembler_state            
        elif state in ['final']:
            self.logger.info('[LoadState] to [FinalState]')
            return self.state_machine.final_state
