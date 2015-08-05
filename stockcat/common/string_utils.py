#-*- coding: utf-8 -*-

import datetime
import re

class NormalizedStringBuilder():
    def build(self, local_string):
        decoded_string = self.__decode(local_string)
        return decoded_string.replace('&nbsp;', ' ')

    # chain of responsibility: try any possible codec
    def __decode(self, local_string):
        try:
            return local_string.decode('big5-hkscs')
        except UnicodeDecodeError:
            return self.__decode_step_1(local_string)

    def __decode_step_1(self, local_string):
        try:
            return local_string.decode('gb18030')
        except UnicodeDecodeError:
            return self.__decode_step_2(local_string)

    def __decode_step_2(self, local_string):
        return local_string.decode('utf-8')

class DateBuilder(): 
    def build(self, local_string):
        try:
            m = re.search(u'(\d+)年(\d+)月(\d+)日', local_string)
            year = int(m.group(1))
            month = int(m.group(2))
            day = int(m.group(3))
            return datetime.date(year, month, day)
        except AttributeError:
            return self.__build_step_1(local_string)

    def __build_step_1(self, local_string):    
        m = re.search('(\d+)/(\d+)/(\d+)', local_string)
        year = int(m.group(1))
        month = int(m.group(2))
        day = int(m.group(3))
        return datetime.date(year, month, day)

class DateIntervalBuilder():
    # chain of responsibility: try any possible pattern
    def build(self, local_string):
        try:
            m = re.search(u'(\d+)年度', local_string)
            year = int(m.group(1))
            return (datetime.date(year, 1, 1), datetime.date(year, 12, 31))
        except AttributeError:
            return self.__build_step_1(local_string)

    def __build_step_1(self, local_string):
        try:
            m = re.search(u'(\d+)年第(\d+)季', local_string)
            whole_year = int(m.group(1))
            end_season = int(m.group(2))
            end_date = self.__from_year_season_to_date(whole_year, end_season)
            return (datetime.date(whole_year, 1, 1), end_date)
        except AttributeError:
            return self.__build_step_2(local_string)

    def __build_step_2(self, local_string):
        m = re.search(u'(\d+)年(\d+)月(\d+)日至(\d+)年(\d+)月(\d+)日', local_string)
        begin_year = int(m.group(1))
        begin_month = int(m.group(2))
        begin_day = int(m.group(3))
        begin_date = datetime.date(begin_year, begin_month, begin_day)
        end_year = int(m.group(4))
        end_month = int(m.group(5))
        end_day = int(m.group(6))
        end_date = datetime.date(end_year, end_month, end_day)
        return (begin_date, end_date)

    def __from_year_season_to_date(self, year, season):
        if season == 1:
            return datetime.date(year, 3, 31)
        if season == 2:
            return datetime.date(year, 6, 30)
        if season == 3:
            return datetime.date(year, 9, 30)
        if season == 4:
            return datetime.date(year, 12, 31)

class StringUtils():
    def __init__(self):
        self.normalized_string_builder = NormalizedStringBuilder()
        self.date_builder = DateBuilder()
        self.date_interval_builder = DateIntervalBuilder()

    def normalize_string(self, local_string):
        return self.normalized_string_builder.build(local_string)

    def normalize_number(self, number_string):
        try:
            return int(number_string.replace(',', ''))
        # number could be float, such as EPS
        except ValueError:
            return float(number_string)

    def from_local_string_to_date(self, local_string):
        return self.date_builder.build(local_string)

    def from_local_string_to_date_interval(self, local_string):
        return self.date_interval_builder.build(local_string)

    def from_date_to_roc_era_string(self, date):
        return str(date.year - 1911)

    def from_date_to_2_digit_month_string(self, date):
        return '{0:02d}'.format(date.month) 

