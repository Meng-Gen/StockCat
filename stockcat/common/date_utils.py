#-*- coding: utf-8 -*-

import calendar
import datetime

class DateUtils():
    def get_first_date_of_month(self, date):
        year = date.year
        month = date.month
        return datetime.date(year, month, 1)

    def get_last_date_of_month(self, date):
        year = date.year
        month = date.month
        day = self.get_last_day_of_month(year, month)
        return datetime.date(year, month, day)

    def get_last_day_of_month(self, year, month):
        return calendar.monthrange(year, month)[1]

    def get_last_date_of_prev_month(self, date):
        return self.get_first_date_of_month(date) - datetime.timedelta(days=1)

    def get_last_date_of_next_month(self, date):
        first_date = self.get_last_date_of_month(date) + datetime.timedelta(days=1)
        return self.get_last_date_of_month(first_date)

    def get_last_date_of_quarter(self, date):
        year = date.year
        quarter = self.get_quarter(date)
        month = 3 * quarter
        return self.get_last_date_of_month(datetime.date(year, month, 1))

    def get_last_date_of_next_quarter(self, date):
        first_date = self.get_last_date_of_quarter(date) + datetime.timedelta(days=1)
        return self.get_last_date_of_quarter(first_date)

    def get_quarter(self, date):
        return (date.month - 1) // 3 + 1

    def range_date_by_month(self, begin_date, end_date):
        curr = self.get_last_date_of_month(begin_date)
        last = self.get_last_date_of_month(end_date)
        month_list = []
        while curr <= last:
            month_list.append(curr)
            curr = self.get_last_date_of_next_month(curr)
        return month_list

    def range_date_by_quarter(self, begin_date, end_date):
        curr = self.get_last_date_of_quarter(begin_date)
        last = self.get_last_date_of_quarter(end_date)
        quarter_list = []
        while curr <= last:
            quarter_list.append(curr)
            curr = self.get_last_date_of_next_quarter(curr)
        return quarter_list
