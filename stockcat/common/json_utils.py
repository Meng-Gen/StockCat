#-*- coding: utf-8 -*-

import datetime
import json
import os
import os.path

class JsonUtils():
    def load(self, path):
        content = None
        with open(path, 'rt') as f:
            content = json.load(f)
        return content

    def save(self, source_json, dest_path):
        # if directory is not existed, need to create by ourselves
        self.__make_directory(dest_path)

        with open(dest_path, 'wt') as f:    
            json.dump(source_json, f)
        
    def filter_key_list(self, json, key_list):
        output = {}
        for key in key_list:
            if key in json:
                output[key] = json[key]
        return output

    def add_type(self, json):
        output = {}
        for key in json:
            value_type = type(json[key])
            if value_type is str:
                output[key] = {
                    'value' : json[key],
                    'type' : 'str',
                }
            elif value_type is unicode:
                output[key] = {
                    'value' : json[key].encode('ascii', 'ignore'),
                    'type' : 'str',
                }
            elif value_type is datetime.date:
                output[key] = {
                    'value' : str(json[key]),
                    'type' : 'datetime.date',
                }
            elif value_type is list:
                output[key] = {
                    'value' : [self.add_type(entry) for entry in json[key]],
                    'type' : 'list',
                }
            else:
                raise ValueError, value_type
        return output

    def remove_type(self, json):
        output = {}
        for key in json:
            value_type, value = json[key]['type'], json[key]['value']
            if value_type == 'str':
                output[key] = value
            elif value_type == 'datetime.date':
                output[key] = self.__get_date_from_string(value)
            elif value_type == 'list':
                output[key] = [self.remove_type(entry) for entry in value]
            else:
                raise ValueError, value_type
        return output

    def __get_date_from_string(self, date_string):
        return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()

    def __make_directory(self, filepath):
        directory = os.path.dirname(os.path.realpath(filepath))
        if not os.path.exists(directory):
            os.makedirs(directory)