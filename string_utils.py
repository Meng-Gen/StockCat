#-*- coding: utf-8 -*-

import datetime
import re

class StringUtils():
    def normalize_string(self, local_string):
        try:
            return local_string.decode('big5').replace('&nbsp;', ' ')
        except UnicodeDecodeError as dummy_error:
            return local_string.decode('gb18030').replace('&nbsp;', ' ')

    def normalize_number(self, number_string):
        return int(number_string.replace(',', ''))

    def from_local_string_to_date(self, local_string):
        p = re.compile(u'(\d+)年(\d+)月(\d+)日')
        result = p.match(local_string)
        year = int(result.group(1))
        month = int(result.group(2))
        day = int(result.group(3))
        return datetime.date(year, month, day)