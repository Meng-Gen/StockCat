#-*- coding: utf-8 -*-

from stockcat.state.aries_memento import AriesMemento
from stockcat.analyzer.stock_symbol_analyzer import StockSymbolAnalyzer

import datetime

class Memento(AriesMemento):
    def __init__(self, path):
        AriesMemento.__init__(self, path)
        self.stock_symbol_list = StockSymbolAnalyzer().get_stock_symbol_list()

    def get_default_value(self):
        print self.stock_symbol_list
        return {
            'state' : 'spider',
            'all_date_list' : list(date_list),
            'todo_date_list' : list(date_list)
        }

    def build_load_value(self, value):
        return {
            'state' : value['state'],
            'all_date_list' : self.get_date_list_from_string_list(value['all_date_list']),
            'todo_date_list' : self.get_date_list_from_string_list(value['todo_date_list']), 
        }

    def build_save_value(self, value):
        return {
            'state' : value['state'],
            'all_date_list' : self.get_string_list_from_date_list(value['all_date_list']),
            'todo_date_list' : self.get_string_list_from_date_list(value['todo_date_list']), 
        }
