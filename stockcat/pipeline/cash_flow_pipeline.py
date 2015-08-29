#-*- coding: utf-8 -*-

from stockcat.pipeline.state.state_machine import StateMachine
from stockcat.pipeline.state.entry_list_helper import EntryListHelper
from stockcat.spider.cash_flow_spider import CashFlowSpider
from stockcat.assembler.cash_flow_assembler import CashFlowAssembler
from stockcat.feed.cash_flow_feed import CashFlowFeedBuilder

import datetime

class CashFlowPipeline(StateMachine):
    def __init__(self, memento_path='./stockcat/data/memento/cash_flow.json'):
        self.helper = EntryListHelper()
        memento_param = {
            'path' : memento_path, 
            'default_value' : self.__get_default_value(),
            'filter_key_list' : [ 'state', 'all_entry_list', 'todo_entry_list', 'last_updated_date' ],
        }
        param = {
            'memento' : memento_param,
            'spider' : CashFlowSpider(), 
            'assembler' : CashFlowAssembler(), 
            'feed_builder' : CashFlowFeedBuilder(),
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
