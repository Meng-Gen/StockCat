#-*- coding: utf-8 -*-

class StockSymbolDao():
    def __init__(self, column_name_list, row_list, release_date):
        self.column_name_list = column_name_list
        self.row_list = row_list
        self.release_date = release_date

    def get_column_name_list(self):
        return self.column_name_list

    def get_row_list(self):
        return self.row_list

    def get_release_date(self):
        return self.release_date
