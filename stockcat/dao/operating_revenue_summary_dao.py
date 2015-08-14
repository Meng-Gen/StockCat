#-*- coding: utf-8 -*-

class OperatingRevenueSummaryDao():
    def __init__(self, column_name_list, row_list, stmt_date, release_date):
        self.column_name_list = column_name_list
        self.row_list = row_list
        self.stmt_date = stmt_date
        self.release_date = release_date

    def get_column_name_list(self):
        return self.column_name_list

    def get_row_list(self):
        return self.row_list

    def get_stmt_date(self):
        return self.stmt_date

    def get_release_date(self):
        return self.release_date
