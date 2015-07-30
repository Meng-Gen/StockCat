#-*- coding: utf-8 -*-

from stockcat.assembler.ifrs_financial_statement_assembler import IfrsFinancialStatementAssembler
from stockcat.common.string_utils import StringUtils
from stockcat.common.file_utils import FileUtils

import datetime

class IfrsFinancialStatementFeed():
    def __init__(self, stock_symbol, date, is_consolidated):
        self.stock_symbol = stock_symbol
        self.year = date.year
        self.season = (date.month - 1) // 3 + 1
        self.report_id = "C" if is_consolidated else "I"
        self.url = self.__build_url()
        self.filepath = self.__build_filepath()

    def get(self):
        self.__copy_url_to_file()
        self.__assemble()

    def __copy_url_to_file(self):
        file_utils = FileUtils()
        file_utils.copy_url_to_file(self.url, self.filepath)
        
    def __assemble(self):
        file_utils = FileUtils()
        content = file_utils.read_file(self.filepath)
        string_utils = StringUtils()
        content = string_utils.normalize_string(content)
        assembler = IfrsFinancialStatementAssembler()
        assembler.assemble(content)

    def __build_url(self):
        return "http://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID=%s&SYEAR=%s&SSEASON=%s&REPORT_ID=%s" \
                % (self.stock_symbol, self.year, self.season, self.report_id)

    def __build_filepath(self):
        return "./stockcat/data/ifrs_financial_statement/all/%s_%s_%s_%s.html" % (self.stock_symbol, self.year, self.season, self.report_id)
