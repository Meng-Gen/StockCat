#-*- coding: utf-8 -*-

from stockcat.state.aries.state_machine import StateMachine
from stockcat.state.aries.entry_list_helper import EntryListHelper
from stockcat.spider.balance_sheet_spider import BalanceSheetSpider
from stockcat.assembler.balance_sheet_assembler import BalanceSheetAssembler
from stockcat.feed.balance_sheet_feed import BalanceSheetFeedBuilder

import datetime

class BalanceSheetStateMachine(StateMachine):
    def __init__(self, memento_path='balance_sheet_memento.json'):
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
        entry_list = self.__get_entry_list()
        # !!! DEBUG ONLY !!!
        entry_list = entry_list[:2]
        return {
            'state' : 'spider',
            'all_entry_list' : list(entry_list),
            'todo_entry_list' : list(entry_list),
            'last_updated_date' : datetime.date(1949, 12, 7) 
        }

    def __get_entry_list(self):
        entry_list = []
        site_begin_date = datetime.date(1996, 3, 31)
        # !!! DEBUG ONLY !!!
        site_begin_date = datetime.date(2014, 3, 31)
        end_date = self.helper.get_now_date()
        for stock_symbol in self.helper.get_stock_symbol_list():
            begin_date = max(site_begin_date, stock_symbol['listing_date'])
            for date in self.helper.get_date_list_by_quarter(begin_date, end_date):
                entry = {
                    'stock_symbol' : stock_symbol['stock_symbol'],
                    'date' : date['date'],
                }
                entry_list.append(entry)
        return entry_list
