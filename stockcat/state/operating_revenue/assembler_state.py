#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class AssemblerState(AriesState):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.spider = state_machine.spider
        self.assembler = state_machine.assembler
        self.todo_entry_list = set()
        self.done_entry_list = set()
        self.dao = {}

    def run(self):
        self.logger.info('run [AssemblerState]')
        self.__set_up()

        # prepare to calculate progress
        entry_count = len(self.todo_entry_list)
        curr_count = 0
        for entry in self.todo_entry_list:
            # update progress
            curr_count += 1
            self.logger.info('assemble operating revenue: {0} (progress: {1}/{2})'.format(entry, curr_count, entry_count))
            
            # prepare dao to hold stock_exchange_market and otc_market
            self.dao[entry] = {}
            
            # assemble stock_exchange_market operating revenue
            content = self.spider.get_crawled('stock_exchange_market', entry)
            self.dao[entry]['stock_exchange_market'] = self.assembler.assemble(content, entry)

            # assemble otc_market operating revenue
            content = self.spider.get_crawled('otc_market', entry)
            self.dao[entry]['otc_market'] = self.assembler.assemble(content, entry)

            # update done_entry_list (will remove from todo_entry_list)
            self.done_entry_list.add(entry)
        self.todo_entry_list = self.todo_entry_list - self.done_entry_list
        
        self.__tear_down()

    def next(self):
        if not self.todo_entry_list:
            self.logger.info('[AssemblerState] to [DatabaseState]')
            return self.state_machine.database_state 
        else:
            return self.state_machine.assembler_state

    def __set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'assembler'
        if value['todo_entry_list']:
            self.todo_entry_list = set(value['todo_entry_list'])
        else:
            self.todo_entry_list = set(value['all_entry_list'])
        self.done_entry_list = set()
        self.state_machine.memento.save()

    def __tear_down(self):
        value = self.state_machine.memento.get_value()
        value['dao'] = self.dao
        value['todo_entry_list'] = list(self.todo_entry_list)
        self.state_machine.memento.save()
