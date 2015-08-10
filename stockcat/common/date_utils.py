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
