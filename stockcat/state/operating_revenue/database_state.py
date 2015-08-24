#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class DatabaseState(AriesState):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.feed_builder = state_machine.feed_builder
        self.database = state_machine.database
        self.todo_entry_list = set()
        self.done_entry_list = set()

    def run(self):
        self.logger.info('run [DatabaseState]')
        self.__set_up()
        
        value = self.state_machine.memento.get_value()

        # prepare to calculate progress
        entry_count = len(self.todo_entry_list)
        curr_count = 0
        for entry in self.todo_entry_list:
            # update progress
            curr_count += 1
            self.logger.info('store operating revenue: {0} (progress: {1}/{2})'.format(entry, curr_count, entry_count))

            # store stock_exchange_market operating revenue            
            feed = self.feed_builder.build(value['dao'][entry]['stock_exchange_market'])
            self.database.store(feed)                
            
            # store otc_market operating revenue            
            feed = self.feed_builder.build(value['dao'][entry]['otc_market'])
            self.database.store(feed)                
            
            # update done_entry_list (will remove from todo_entry_list)
            self.done_entry_list.add(entry)
        self.todo_entry_list = self.todo_entry_list - self.done_entry_list
        
        self.__tear_down()

    def next(self):
        if not self.todo_entry_list:
            self.logger.info('[DatabaseState] to [FinalState]')
            return self.state_machine.final_state 
        else:
            return self.state_machine.database_state

    def __set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'database'
        if value['todo_entry_list']:
            self.todo_entry_list = set(value['todo_entry_list'])
        else:
            self.todo_entry_list = set(value['all_entry_list'])
        self.done_entry_list = set()
        self.state_machine.memento.save()

    def __tear_down(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'final'
        value['todo_entry_list'] = list(self.todo_entry_list)
        self.state_machine.memento.save()
