#-*- coding: utf-8 -*-

from stockcat.assembler.legacy.cash_flow_parser.aries_parser import AriesParser
from stockcat.common.string_utils import StringUtils
from stockcat.dao.cash_flow_dao import CashFlowDao

import lxml.html

class LegacyCashFlowAssembler():
    def __init__(self):
        self.base_xpath = '//html/body/table[@class="hasBorder"]/tr/td/pre'
        self.string_utils = StringUtils()

    def assemble(self, param):
        content, stock_symbol, date = param['content'], param['stock_symbol'], param['date']
        content = self.string_utils.normalize_string(content)
        html_object = lxml.html.fromstring(content)
        relative_html_object = self.__traverse_to_relative_html_object(html_object)
        # Parse cash flow statement 
        column_name_list, row_list = self.__assemble_summary(relative_html_object.text)
        return CashFlowDao(column_name_list, row_list, stock_symbol, date)

    def __traverse_to_relative_html_object(self, html_object):
        relative_html_object_list = html_object.xpath(self.base_xpath)
        assert len(relative_html_object_list) == 1, 'invalid base_xpath'
        return relative_html_object_list[0]

    def __assemble_summary(self, text):
        return AriesParser(text).parse()
        