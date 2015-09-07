#-*- coding: utf-8 -*-

from stockcat.pipeline.state.state import State

import logging

class DatabaseState(State):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.feed_builder = state_machine.feed_builder
        self.database = state_machine.database
        self.todo_entry_list = None

    def run(self):
        self.logger.info('run database state')
        self.set_up()

        dao = self.state_machine.get_value('dao')

        # prepare to calculate progress
        undone_entry_list = list(self.todo_entry_list)
        entry_count = len(undone_entry_list)
        curr_count = 0
        for entry in undone_entry_list:
            # update progress
            curr_count += 1
            self.logger.info('store: {0} (progress: {1}/{2})'.format(entry, curr_count, entry_count))

            # store
            feed = self.feed_builder.build(dao[str(entry)])
            self.database.store(feed)                

            # update todo entry list
            self.todo_entry_list.remove(entry)

            # avoid exceptional shutdown
            if curr_count % 10 == 0:
                self.tear_down()

        self.tear_down()

        if not self.todo_entry_list:
            self.logger.info('move database state to final state')        
            self.state_machine.set_value('transition_value', '')
        else:
            self.logger.error('run database state again (?)')        
            self.state_machine.set_value('transition_value', 'error')

    def set_up(self):
        self.state_machine.set_value('state', 'database')
        todo_entry_list = self.state_machine.get_value('todo_entry_list')
        all_entry_list = self.state_machine.get_value('all_entry_list')
        if todo_entry_list:
            self.todo_entry_list = list(todo_entry_list)
        else:
            self.todo_entry_list = list(all_entry_list)
        self.state_machine.save_memento()

    def tear_down(self):
        self.state_machine.set_value('state', 'final')
        self.state_machine.set_value('todo_entry_list', list(self.todo_entry_list))
        self.state_machine.save_memento()
