#-*- coding: utf-8 -*-

from balance_sheet_assembler import BalanceSheetAssembler
from income_statement_assembler import IncomeStatementAssembler
from cash_flow_statement_assembler import CashFlowStatementAssembler

import lxml.html

class FinancialStatementAssembler():
    def assemble(self, content):
        html_object = lxml.html.fromstring(content)
        balance_sheet = BalanceSheetAssembler().assemble(html_object)
        income_statement = IncomeStatementAssembler().assemble(html_object)
        cash_flow_statement = CashFlowStatementAssembler().assemble(html_object)

        print balance_sheet
        print income_statement
        print cash_flow_statement
