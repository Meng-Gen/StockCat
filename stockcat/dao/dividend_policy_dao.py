#-*- coding: utf-8 -*-

class DividendPolicyDao():
    def __init__(self, column_name_list, row_list, stock_symbol):
        self.column_name_list = column_name_list
        self.row_list = row_list
        self.stock_symbol = stock_symbol

    def get_column_name_list(self):
        return self.column_name_list

    def get_row_list(self):
        return self.row_list

    def get_stock_symbol(self):
        return self.stock_symbol
