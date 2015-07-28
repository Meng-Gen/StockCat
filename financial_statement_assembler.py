#-*- coding: utf-8 -*-

from balance_sheet_assembler import BalanceSheetAssembler

import lxml.html

class FinancialStatementAssembler():
    def assemble(self, content):
        html_object = lxml.html.fromstring(content)
        balance_sheet = self.__assemble_balance_sheet(html_object)
        print balance_sheet

    def __assemble_balance_sheet(self, html_object):
        assembler = BalanceSheetAssembler()
        return assembler.assemble(html_object)
