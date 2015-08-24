#-*- coding: utf-8 -*-

from stockcat.state.aries_state import AriesState

import logging

class DatabaseState(AriesState):
    def __init__(self, state_machine, feed_builder, database):
        self.logger = logging.getLogger(__name__)
        self.state_machine = state_machine
        self.feed_builder = feed_builder
        self.database = database
        self.todo_date_list = set()
        self.done_date_list = set()

    def run(self):
        self.logger.info('run [DatabaseState]')
        self.__set_up()
        value = self.state_machine.memento.get_value()
        for todo_date in self.todo_date_list:
            self.logger.info('store operating revenue: {0}'.format(todo_date))
            feed = self.feed_builder.build(value['dao'][todo_date]['stock_exchange_market'])
            self.database.store(feed)                
            feed = self.feed_builder.build(value['dao'][todo_date]['otc_market'])
            self.database.store(feed)                
            self.done_date_list.add(todo_date)
        self.todo_date_list = self.todo_date_list - self.done_date_list
        self.__tear_down()

    def next(self):
        if not self.todo_date_list:
            self.logger.info('[DatabaseState] to [FinalState]')
            return self.state_machine.final_state 
        else:
            return self.state_machine.database_state

    def __set_up(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'database'
        if value['todo_date_list']:
            self.todo_date_list = set(value['todo_date_list'])
        else:
            self.todo_date_list = set(value['all_date_list'])
        self.done_date_list = set()
        self.state_machine.memento.save()

    def __tear_down(self):
        value = self.state_machine.memento.get_value()
        value['state'] = 'final'
        value['todo_date_list'] = list(self.todo_date_list)
        self.state_machine.memento.save()
