#-*- coding: utf-8 -*-

from stockcat.pipeline.state.state import State

import logging

class AssemblerState(State):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.spider = state_machine.spider
        self.assembler = state_machine.assembler
        self.todo_entry_list = None
        self.dao = {}

    def run(self):
        self.logger.info('run assembler state')
        self.set_up()

        # prepare to calculate progress
        undone_entry_list = list(self.todo_entry_list)
        entry_count = len(undone_entry_list)
        curr_count = 0
        for entry in undone_entry_list:
            # update progress
            curr_count += 1
            self.logger.info('assemble: {0} (progress: {1}/{2})'.format(entry, curr_count, entry_count))

            try:
                # assemble 
                internal_entry = dict(entry)
                internal_entry['content'] = self.spider.get_crawled(internal_entry)
                # build hashable string because dict is unhashable
                self.dao[str(entry)] = self.assembler.assemble(internal_entry)
            except Exception as e:
                self.logger.error(e)

            # avoid exceptional shutdown
            if curr_count % 10 == 0:
                self.tear_down()

            # update todo entry list
            self.todo_entry_list.remove(entry)
        
        self.tear_down()

        if not self.todo_entry_list:
            self.logger.info('move assembler state to database state')        
            self.state_machine.set_value('transition_value', '')
        else:
            self.logger.error('run assembler state again (?)')        
            self.state_machine.set_value('transition_value', 'error')

    def set_up(self):
        self.state_machine.set_value('state', 'assembler')
        todo_entry_list = self.state_machine.get_value('todo_entry_list')
        all_entry_list = self.state_machine.get_value('all_entry_list')
        if todo_entry_list:
            self.todo_entry_list = list(todo_entry_list)
        else:
            self.todo_entry_list = list(all_entry_list)
        self.state_machine.save_memento()

    def tear_down(self):
        self.state_machine.set_value('todo_entry_list', list(self.todo_entry_list))
        self.state_machine.set_value('dao', self.dao)
        self.state_machine.save_memento()
