#-*- coding: utf-8 -*-

from stockcat.state.aries_memento import AriesMemento
from stockcat.analyzer.stock_symbol_analyzer import StockSymbolAnalyzer

import datetime

class Memento(AriesMemento):
    def __init__(self, path):
        AriesMemento.__init__(self, path)

    def get_default_value(self):
        all_entry_list = self.__get_param_list()[:1]
        return {
            'state' : 'spider',
            'all_entry_list' : list(all_entry_list),
            'todo_entry_list' : list(all_entry_list)
        }

    def build_load_value(self, value):
        return {
            'state' : value['state'],
            'all_entry_list' : value['all_entry_list'],
            'todo_entry_list' : value['todo_entry_list'], 
        }

    def build_save_value(self, value):
        return {
            'state' : value['state'],
            'all_entry_list' : value['all_entry_list'],
            'todo_entry_list' : value['todo_entry_list'], 
        }

    def __get_param_list(self):
        entry_list = StockSymbolAnalyzer().get_stock_symbol_list()
        param_list = []
        for entry in entry_list:
            stock_symbol = entry[0]
            param = {
                'stock_symbol' : {
                    'value' : entry[0],
                    'type' : 'string',
                },
            }
            param_list.append(param)
        return param_list
