#-*- coding: utf-8 -*-

from stockcat.state.aries.state import State

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

            # wait for next entry
            self.avoid_blocking()

        self.tear_down()

    def next(self):
        if not self.todo_entry_list:
            self.logger.info('move spider state to assembler state')        
            return self.state_machine.assembler_state            
        else:
            self.logger.error('run spider state again (?)')        
            return self.state_machine.spider_state

    def set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'spider'
        if value['todo_entry_list']:
            self.todo_entry_list = list(value['todo_entry_list'])
        else:
            self.todo_entry_list = list(value['all_entry_list'])
        self.last_updated_date = value['last_updated_date']
        self.state_machine.memento.save()

    def tear_down(self):
        value = self.state_machine.memento.get_value()
        value['todo_entry_list'] = list(self.todo_entry_list)
        value['last_updated_date'] = self.last_updated_date
        self.state_machine.memento.save()
