#-*- coding: utf-8 -*-

from stockcat.dao.operating_revenue_dao import OperatingRevenueDao

class Database():
    def insert_operating_revenue(self, dao):
        print dao.get_stock_symbol()
        print dao.get_date()
        print dao.get_column_name_list()[0], dao.get_column_name_list()[1]
        for row in dao.get_row_list():
            print row[0], row[1]