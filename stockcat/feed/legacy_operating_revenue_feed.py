#-*- coding: utf-8 -*-

from stockcat.assembler.legacy_operating_revenue_assembler import LegacyOperatingRevenueAssembler
from stockcat.common.string_utils import StringUtils
from stockcat.common.file_utils import FileUtils

import datetime

class LegacyOperatingRevenueFeed():
    def __init__(self, stock_symbol, date):
        self.string_utils = StringUtils()
        self.file_utils = FileUtils()

        self.stock_symbol = stock_symbol
        self.year = self.string_utils.from_date_to_roc_era_string(date)
        self.month = self.string_utils.from_date_to_2_digit_month_string(date)
        self.url = self.__build_url()
        self.filepath = self.__build_filepath()

    def get(self):
        #self.__copy_url_to_file()
        self.__assemble()

    def __copy_url_to_file(self):
        self.file_utils.copy_url_to_file(self.url, self.filepath)
        
    def __assemble(self):
        content = self.file_utils.read_file(self.filepath)
        content = self.string_utils.normalize_string(content)
        assembler = LegacyOperatingRevenueAssembler()
        return assembler.assemble(content)

    def __build_url(self):
        # do not forget escape %
        return "http://mops.twse.com.tw/mops/web/ajax_t05st10?encodeURIComponent=1&run=Y&step=0&colorchg=&TYPEK=sii%%20&co_id=%s&off=1&year=%s&month=%s&firstin=true" \
                % (self.stock_symbol, self.year, self.month)

    def __build_filepath(self):
        return "./stockcat/data/legacy_operating_revenue/%s_%s_%s.html" % (self.stock_symbol, self.year, self.month)
