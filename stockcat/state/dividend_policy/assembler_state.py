#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class AssemblerState(AriesState):
    def __init__(self, state_machine, spider, assembler):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.spider = spider
        self.assembler = assembler
        self.todo_date_list = set()
        self.done_date_list = set()
        self.dao = {}

    def run(self):
        self.logger.info('run [AssemblerState]')
        self.__set_up()
        for todo_date in self.todo_date_list:
            self.logger.info('assembler operating revenue: {0}'.format(todo_date))
            self.dao[todo_date] = {}
            content = self.spider.get_crawled('stock_exchange_market', todo_date)
            self.dao[todo_date]['stock_exchange_market'] = self.assembler.assemble(content, todo_date)
            content = self.spider.get_crawled('otc_market', todo_date)
            self.dao[todo_date]['otc_market'] = self.assembler.assemble(content, todo_date)
            self.done_date_list.add(todo_date)
        self.todo_date_list = self.todo_date_list - self.done_date_list
        self.__tear_down()

    def next(self):
        if not self.todo_date_list:
            self.logger.info('[AssemblerState] to [DatabaseState]')
            return self.state_machine.database_state 
        else:
            return self.state_machine.assembler_state

    def __set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'assembler'
        if value['todo_date_list']:
            self.todo_date_list = set(value['todo_date_list'])
        else:
            self.todo_date_list = set(value['all_date_list'])
        self.done_date_list = set()
        self.state_machine.memento.save()

    def __tear_down(self):
        value = self.state_machine.memento.get_value()
        value['dao'] = self.dao
        value['todo_date_list'] = list(self.todo_date_list)
        self.state_machine.memento.save()
