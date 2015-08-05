#-*- coding: utf-8 -*-

from stockcat.common.file_utils import FileUtils
from stockcat.common.string_utils import StringUtils
from stockcat.assembler.stock_symbol_assembler import StockSymbolAssembler

import datetime

class OtcMarketFeed():
    def __init__(self):
        self.url = self.__build_url()
        self.filepath = self.__build_filepath()

    def get(self):
        #self.__copy_url_to_file()
        self.__assemble()

    def __copy_url_to_file(self):
        file_utils = FileUtils()
        file_utils.copy_url_to_file(self.url, self.filepath)

    def __assemble(self):
        file_utils = FileUtils()
        content = file_utils.read_file(self.filepath)
        string_utils = StringUtils()
        content = string_utils.normalize_string(content)
        assembler = StockSymbolAssembler()
        return assembler.assemble(content)

    def __build_url(self):
        return "http://isin.twse.com.tw/isin/C_public.jsp?strMode=4"

    def __build_filepath(self):
        return "./stockcat/data/stock_symbol/otc_market.html"
