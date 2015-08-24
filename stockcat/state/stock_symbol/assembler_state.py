#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class AssemblerState(AriesState):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.spider = state_machine.spider
        self.assembler = state_machine.assembler
        self.dao = {}

    def run(self):
        self.logger.info('run [AssemblerState]')
        self.__set_up()
        self.logger.info('assemble stock exchange market stock symbol')
        self.dao['stock_exchange_market'] = self.assembler.assemble(self.spider.get_crawled('stock_exchange_market'))        
        self.logger.info('assemble otc market stock symbol')
        self.dao['otc_market'] = self.assembler.assemble(self.spider.get_crawled('otc_market'))        
        self.__tear_down()

    def next(self):
        self.logger.info('[AssemblerState] to [DatabaseState]')
        return self.state_machine.database_state 

    def __set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'assembler'
        self.state_machine.memento.save()

    def __tear_down(self):
        value = self.state_machine.memento.get_value()
        value['dao'] = self.dao
        value['release_date'] = self.dao['stock_exchange_market'].get_release_date()
        self.state_machine.memento.save()
