#-*- coding: utf-8 -*-

from stockcat.assembler.ifrs_balance_sheet_assembler import IfrsBalanceSheetAssembler
from stockcat.assembler.ifrs_income_statement_assembler import IfrsIncomeStatementAssembler
from stockcat.assembler.ifrs_cash_flow_statement_assembler import IfrsCashFlowStatementAssembler

import lxml.html

class IfrsFinancialStatementAssembler():
    def assemble(self, content):
        html_object = lxml.html.fromstring(content)
        balance_sheet = IfrsBalanceSheetAssembler().assemble(html_object)
        income_statement = IfrsIncomeStatementAssembler().assemble(html_object)
        cash_flow_statement = IfrsCashFlowStatementAssembler().assemble(html_object)

        #print balance_sheet
        #print income_statement
        #print cash_flow_statement
