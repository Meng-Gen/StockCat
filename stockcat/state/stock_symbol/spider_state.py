#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class SpiderState(AriesState):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.spider = state_machine.spider

    def run(self):
        self.logger.info('run [SpiderState]')
        self.__set_up()
        self.logger.info('crawl stock exchange market stock symbol')
        self.spider.crawl('stock_exchange_market')
        self.avoid_blocking()
        self.logger.info('crawl otc market stock symbol')
        self.spider.crawl('otc_market')
        self.__tear_down()

    def next(self):
        self.logger.info('[SpiderState] to [AssemblerState]')        
        return self.state_machine.assembler_state            

    def __set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'spider'
        self.state_machine.memento.save()

    def __tear_down(self):
        pass