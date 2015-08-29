#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class DatabaseState(AriesState):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.feed_builder = state_machine.feed_builder
        self.database = state_machine.database
        self.todo_entry_list = None
        self.done_entry_list = None
        self.dao_list = None

    def run(self):
        self.logger.info('run database state')
        self.__set_up()

        value = self.state_machine.memento.get_value()

        # prepare to calculate progress
        done_entry_list = []
        undone_entry_list = list(self.todo_entry_list)
        entry_count = len(self.todo_entry_list)
        curr_count = 0
        for entry in self.todo_entry_list:
            # update progress
            curr_count += 1
            self.logger.info('store: {0} (progress: {1}/{2})'.format(entry, curr_count, entry_count))

            # store
            feed = self.feed_builder.build(value['dao'][str(entry)])
            self.database.store(feed)                

            # update done/undone entry list
            done_entry_list.append(entry)
            undone_entry_list.remove(entry)
        self.done_entry_list = list(done_entry_list)
        self.todo_entry_list = list(undone_entry_list)

        self.__tear_down()

    def next(self):
        if not self.todo_entry_list:
            self.logger.info('move database_state to final_state')
            return self.state_machine.final_state 
        else:
            self.logger.error('run database state again (?)')        
            return self.state_machine.database_state

    def __set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'database'
        if value['todo_entry_list']:
            self.todo_entry_list = list(value['todo_entry_list'])
        else:
            self.todo_entry_list = list(value['all_entry_list'])
        self.done_entry_list = []
        self.state_machine.memento.save()

    def __tear_down(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'final'
        value['todo_entry_list'] = list(self.todo_entry_list)
        value['done_entry_list'] = list(self.done_entry_list)
        self.state_machine.memento.save()
