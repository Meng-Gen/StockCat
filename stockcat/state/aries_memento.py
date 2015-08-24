#-*- coding: utf-8 -*-

import datetime
import json
import logging
import os

class AriesMemento():
    def __init__(self, path):
        self.logger = logging.getLogger(__name__)
        self.path = path
        self.value = None
        self.latest_loaded_value = None

    def load(self):
        self.logger.info('load memento')
        if os.path.exists(self.path):
            with open(self.path, 'rt') as f:
                try:
                    self.value = self.build_load_value(json.load(f))
                except ValueError as e:
                    self.logger.error('failed to load memento (use default instead)', exc_info=True)
                    self.value = self.get_default_value()
                except KeyError as e:
                    self.logger.error('failed to build load value (use default instead)', exc_info=True)
                    self.value = self.get_default_value()
        else:
            self.value = self.get_default_value()
        self.latest_loaded_value = dict(self.value)

    def save(self):
        self.logger.info('save memento')
        with open(self.path, 'wt') as f:
            try:
                json.dump(self.build_save_value(self.value), f)
            except TypeError as e:
                self.logger.error('failed to load memento (use default instead)', exc_info=True)
                json.dump(self.build_save_value(self.latest_loaded_value), f)

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_date_list_from_string_list(self, string_list):
        return [self.get_date_from_string(string) for string in string_list]

    def get_string_list_from_date_list(self, date_list):
        return [str(date) for date in date_list]

    def get_date_from_string(self, date_string):
        return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()

    def get_default_value(self):
        raise NotImplementedError, 'we should implement the abstract method' 

    def build_load_value(self, value):
        raise NotImplementedError, 'we should implement the abstract method' 

    def build_save_value(self, value):
        raise NotImplementedError, 'we should implement the abstract method' 
