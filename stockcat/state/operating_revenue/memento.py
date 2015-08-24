#-*- coding: utf-8 -*-

from stockcat.state.aries_memento import AriesMemento

import datetime

class Memento(AriesMemento):
    def __init__(self, path):
        AriesMemento.__init__(self, path)

    def get_default_value(self):
        return {
            'state' : 'spider',
            'all_date_list' : [datetime.date(2015, 1, 31), datetime.date(2015, 2, 28)],
            'todo_date_list' : [datetime.date(2015, 1, 31), datetime.date(2015, 2, 28)],
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
