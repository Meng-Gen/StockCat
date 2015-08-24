#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class DatabaseState(AriesState):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.feed_builder = state_machine.feed_builder
        self.database = state_machine.database

    def run(self):
        self.logger.info('run [DatabaseState]')
        self.__set_up()
        value = self.state_machine.memento.get_value()
        self.logger.info('store stock exchange market stock symbol')
        feed = self.feed_builder.build(value['dao']['stock_exchange_market'])
        self.database.store(feed)
        self.logger.info('store otc market stock symbol')
        feed = self.feed_builder.build(value['dao']['otc_market'])
        self.database.store(feed)
        self.__tear_down()

    def next(self):
        self.logger.info('[DatabaseState] to [FinalState]')
        return self.state_machine.final_state 

    def __set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'database'
        self.state_machine.memento.save()

    def __tear_down(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'final'
        self.state_machine.memento.save()
