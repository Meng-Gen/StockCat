#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class SpiderState(AriesState):
    def __init__(self, state_machine, spider):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.spider = spider
        self.todo_date_list = set()
        self.done_date_list = set()

    def run(self):
        self.logger.info('run [SpiderState]')
        self.__set_up()
        for todo_date in self.todo_date_list:
            self.logger.info('crawl operating revenue: {0}'.format(todo_date))
            self.avoid_blocking()
            self.done_date_list.add(todo_date)
        self.todo_date_list = self.todo_date_list - self.done_date_list
        self.__tear_down()

    def next(self):
        if not self.todo_date_list:
            self.logger.info('[SpiderState] to [AssemblerState]')
            return self.state_machine.assembler_state            
        else:
            return self.state_machine.spider_state

    def __set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'spider'
        if value['todo_date_list']:
            self.todo_date_list = set(value['todo_date_list'])
        else:
            self.todo_date_list = set(value['all_date_list'])
        self.done_date_list = set()
        self.state_machine.memento.save()

    def __tear_down(self):
        value = self.state_machine.memento.get_value()
        value['todo_date_list'] = list(self.todo_date_list)
        self.state_machine.memento.save()
