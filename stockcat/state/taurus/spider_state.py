#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class SpiderState(AriesState):
    def __init__(self, state_machine):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.spider = state_machine.spider
        self.todo_entry_list = set()
        self.done_entry_list = set()

    def run(self):
        self.logger.info('run [SpiderState]')
        self.__set_up()

        # prepare to calculate progress
        entry_count = len(self.todo_entry_list)
        curr_count = 0
        for entry in self.todo_entry_list:
            # update progress
            curr_count += 1
            self.logger.info('crawl dividend policy: {0} (progress: {1}/{2})'.format(entry, curr_count, entry_count))
            
            # crawl dividend policy
            self.spider.crawl(entry)
            self.avoid_blocking()
        
            # update done_entry_list (will remove from todo_entry_list)
            self.done_entry_list.add(entry)
        self.todo_entry_list = self.todo_entry_list - self.done_entry_list
        
        self.__tear_down()

    def next(self):
        if not self.todo_entry_list:
            self.logger.info('[SpiderState] to [AssemblerState]')
            return self.state_machine.assembler_state            
        else:
            return self.state_machine.spider_state

    def __set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'spider'
        if value['todo_entry_list']:
            self.todo_entry_list = set(value['todo_entry_list'])
        else:
            self.todo_entry_list = set(value['all_entry_list'])
        self.done_entry_list = set()
        self.state_machine.memento.save()

    def __tear_down(self):
        value = self.state_machine.memento.get_value()
        value['todo_entry_list'] = list(self.todo_entry_list)
        self.state_machine.memento.save()