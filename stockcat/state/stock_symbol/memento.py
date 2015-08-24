#-*- coding: utf-8 -*-

from stockcat.state.aries_memento import AriesMemento

import datetime

class Memento(AriesMemento):
    def __init__(self, path):
        AriesMemento.__init__(self, path)

    def get_default_value(self):
        return {
            'state' : 'spider',
            'release_date' : datetime.date(1949, 12, 7),
        }
    
    def build_load_value(self, value):
        return {
            'state' : value['state'],
            'release_date' : self.get_date_from_string(value['release_date']),
        }

    def build_save_value(self, value):
        return {
            'state' : value['state'],
            'release_date' : str(value['release_date']),
        }
