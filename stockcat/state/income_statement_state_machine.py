#-*- coding: utf-8 -*-

from stockcat.state.aries.state_machine import StateMachine
from stockcat.state.aries.entry_list_helper import EntryListHelper
from stockcat.spider.income_statement_spider import IncomeStatementSpider
from stockcat.assembler.income_statement_assembler import IncomeStatementAssembler
from stockcat.feed.income_statement_feed import IncomeStatementFeedBuilder

import datetime

class IncomeStatementStateMachine(StateMachine):
    def __init__(self, memento_path='income_statement_memento.json'):
        self.helper = EntryListHelper()
        memento_param = {
            'path' : memento_path, 
            'default_value' : self.__get_default_value(),
            'filter_key_list' : [ 'state', 'all_entry_list', 'todo_entry_list', 'last_updated_date' ],
        }
        param = {
            'memento' : memento_param,
            'spider' : IncomeStatementSpider(), 
            'assembler' : IncomeStatementAssembler(), 
            'feed_builder' : IncomeStatementFeedBuilder(),
        }
        StateMachine.__init__(self, param)

    def __get_default_value(self):
        all_entry_list = self.helper.get_all_financial_statement_entry_list()
        todo_entry_list = self.helper.get_legacy_financial_statement_entry_list()
        # !!! DEBUG ONLY !!!
        all_entry_list = all_entry_list[67:68]
        todo_entry_list = todo_entry_list[67:68]
        return {
            'state' : 'spider',
            'all_entry_list' : list(all_entry_list),
            'todo_entry_list' : list(todo_entry_list),
            'last_updated_date' : datetime.date(1949, 12, 7) 
        }
