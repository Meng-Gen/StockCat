#-*- coding: utf-8 -*-

import datetime

class OperatingRevenueDao():
    def __init__(self, column_name_list, row_list):
        self.column_name_list = column_name_list
        self.row_list = row_list

    def get_column_name_list(self):
        return self.column_name_list

    def get_row_list(self):
        return self.row_list
     