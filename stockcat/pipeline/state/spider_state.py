#-*- coding: utf-8 -*-

from stockcat.pipeline.state.state import State

import logging

class SpiderState(State):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.spider = state_machine.spider
        self.todo_entry_list = None
        self.last_updated_date = None

    def run(self):
        self.logger.info('run spider state')
        self.set_up()

        # prepare to calculate progress
        undone_entry_list = list(self.todo_entry_list)
        entry_count = len(undone_entry_list)
        curr_count = 0
        for entry in undone_entry_list:
            # update progress
            curr_count += 1
            self.logger.info('crawl: {0} (progress: {1}/{2})'.format(entry, curr_count, entry_count))

            # crawl 
            self.spider.crawl(entry)

            # update todo entry list
            self.todo_entry_list.remove(entry)

            # avoid exceptional shutdown
            if curr_count % 10 == 0:
                self.tear_down()

            # wait for next entry
            self.avoid_blocking()

        self.tear_down()

        if not self.todo_entry_list:
            self.logger.info('move spider state to assembler state')
            self.state_machine.set_value('transition_value', '')
        else:
            self.logger.error('run spider state again (?)')        
            self.state_machine.set_value('transition_value', 'error')

    def set_up(self):
        self.state_machine.set_value('state', 'spider')
        todo_entry_list = self.state_machine.get_value('todo_entry_list')
        all_entry_list = self.state_machine.get_value('all_entry_list')
        if todo_entry_list:
            self.todo_entry_list = list(todo_entry_list)
        else:
            self.todo_entry_list = list(all_entry_list)
        self.last_updated_date = self.state_machine.get_value('last_updated_date')
        self.state_machine.save_memento()

    def tear_down(self):
        self.state_machine.set_value('todo_entry_list', list(self.todo_entry_list))
        self.state_machine.set_value('last_updated_date', self.last_updated_date)
        self.state_machine.save_memento()
