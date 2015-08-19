#-*- coding: utf-8 -*-

from stockcat.assembler.operating_revenue_summary.aries_parser import AriesParser
from stockcat.assembler.operating_revenue_summary.taurus_parser import TaurusParser
from stockcat.assembler.operating_revenue_summary.gemini_parser import GeminiParser
from stockcat.assembler.operating_revenue_summary.cancer_parser import CancerParser
from stockcat.assembler.operating_revenue_summary.leo_parser import LeoParser
from stockcat.assembler.content_screener import ContentScreener
from stockcat.common.date_utils import DateUtils
from stockcat.common.string_utils import StringUtils
from stockcat.dao.operating_revenue_summary_dao import OperatingRevenueSummaryDao

import lxml.html     

class OperatingRevenueSummaryAssembler():
    def __init__(self):
        self.content_screener = ContentScreener()
        self.date_utils = DateUtils()
        self.string_utils = StringUtils()

    def assemble(self, content, date):
        self.content_screener.screen(content, { 'date' : date })
        stmt_date = self.date_utils.get_last_date_of_month(date)
        column_name_list, row_list, release_date = self.__assemble_summary(content)
        return OperatingRevenueSummaryDao(column_name_list, row_list, stmt_date, release_date)

    def __assemble_summary(self, html_object):
        try:
            return AriesParser().parse(html_object)
        except AssertionError:
            return self.__assemble_summary_step_1(html_object)

    def __assemble_summary_step_1(self, html_object):
        try:
            return TaurusParser().parse(html_object)
        except AssertionError:
            return self.__assemble_summary_step_2(html_object)

    def __assemble_summary_step_2(self, html_object):
        try:
            return GeminiParser().parse(html_object)
        except AssertionError:
            return self.__assemble_summary_step_3(html_object)

    def __assemble_summary_step_3(self, html_object):
        try:
            return CancerParser().parse(html_object)
        except AssertionError:
            return LeoParser().parse(html_object)
