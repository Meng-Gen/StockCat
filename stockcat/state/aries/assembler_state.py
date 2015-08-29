#-*- coding: utf-8 -*-

from stockcat.state.aries.state import State

import logging

class AssemblerState(State):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.spider = state_machine.spider
        self.assembler = state_machine.assembler
        self.todo_entry_list = None
        self.done_entry_list = None
        self.dao = {}

    def run(self):
        self.logger.info('run assembler state')
        self.__set_up()

        # prepare to calculate progress
        done_entry_list = []
        undone_entry_list = list(self.todo_entry_list)
        entry_count = len(self.todo_entry_list)
        curr_count = 0
        for entry in self.todo_entry_list:
            # update progress
            curr_count += 1
            self.logger.info('assemble: {0} (progress: {1}/{2})'.format(entry, curr_count, entry_count))
            
            # assemble 
            internal_entry = dict(entry)
            internal_entry['content'] = self.spider.get_crawled(internal_entry)
            # build hashable string because dict is unhashable
            self.dao[str(entry)] = self.assembler.assemble(internal_entry)

            # update done/undone entry list
            done_entry_list.append(entry)
            undone_entry_list.remove(entry)
        self.done_entry_list = list(done_entry_list)
        self.todo_entry_list = list(undone_entry_list)
        
        self.__tear_down()

    def next(self):
        if not self.todo_entry_list:
            self.logger.info('move assembler state to database state')        
            return self.state_machine.database_state            
        else:
            self.logger.error('run assembler state again (?)')        
            return self.state_machine.spider_state

    def __set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'assembler'
        if value['todo_entry_list']:
            self.todo_entry_list = list(value['todo_entry_list'])
        else:
            self.todo_entry_list = list(value['all_entry_list'])
        self.done_entry_list = []
        self.dao_list = []
        self.state_machine.memento.save()

    def __tear_down(self):
        value = self.state_machine.memento.get_value()
        value['todo_entry_list'] = list(self.todo_entry_list)
        value['done_entry_list'] = list(self.done_entry_list)
        value['dao'] = self.dao
        self.state_machine.memento.save()
