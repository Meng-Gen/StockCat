#-*- coding: utf-8 -*-

from stockcat.pipeline.state.state_machine import StateMachine
from stockcat.pipeline.state.entry_list_helper import EntryListHelper
from stockcat.spider.balance_sheet_spider import BalanceSheetSpider
from stockcat.assembler.balance_sheet_assembler import BalanceSheetAssembler
from stockcat.feed.balance_sheet_feed import BalanceSheetFeedBuilder

import datetime

class BalanceSheetPipeline(StateMachine):
    def __init__(self, memento_path='./stockcat/data/memento/balance_sheet.json'):
        self.helper = EntryListHelper()
        memento_param = {
            'path' : memento_path, 
            'default_value' : self.__get_default_value(),
            'filter_key_list' : [ 'state', 'all_entry_list', 'todo_entry_list', 'last_updated_date' ],
        }
        param = {
            'memento' : memento_param,
            'spider' : BalanceSheetSpider(), 
            'assembler' : BalanceSheetAssembler(), 
            'feed_builder' : BalanceSheetFeedBuilder(),
        }
        StateMachine.__init__(self, param)

    def __get_default_value(self):
        all_entry_list = self.helper.get_all_financial_statement_entry_list()
        # !!! DEBUG ONLY !!!
        all_entry_list = all_entry_list[67:68]
        return {
            'state' : 'spider',
            'all_entry_list' : list(all_entry_list),
            'todo_entry_list' : list(all_entry_list),
            'last_updated_date' : datetime.date(1949, 12, 7) 
        }
