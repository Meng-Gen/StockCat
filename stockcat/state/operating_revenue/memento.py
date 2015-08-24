#-*- coding: utf-8 -*-

from stockcat.state.aries_memento import AriesMemento
from stockcat.common.date_utils import DateUtils

import datetime

class Memento(AriesMemento):
    def __init__(self, path):
        AriesMemento.__init__(self, path)
        self.date_utils = DateUtils()

    def get_default_value(self):
        begin_date = datetime.date(2010, 6, 30)
        end_date = self.date_utils.now_date()
        date_list = list(self.date_utils.range_date_by_month(begin_date, end_date))[:1]
        return {
            'state' : 'spider',
            'all_entry_list' : list(date_list),
            'todo_entry_list' : list(date_list)
        }

    def build_load_value(self, value):
        return {
            'state' : value['state'],
            'all_entry_list' : self.get_date_list_from_string_list(value['all_entry_list']),
            'todo_entry_list' : self.get_date_list_from_string_list(value['todo_entry_list']), 
        }

    def build_save_value(self, value):
        return {
            'state' : value['state'],
            'all_entry_list' : self.get_string_list_from_date_list(value['all_entry_list']),
            'todo_entry_list' : self.get_string_list_from_date_list(value['todo_entry_list']), 
        }
