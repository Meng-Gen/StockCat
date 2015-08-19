#-*- coding: utf-8 -*-

from stockcat.assembler.xbrl.xbrl_income_statement_assembler import XbrlIncomeStatementAssembler
from stockcat.assembler.legacy.legacy_income_statement_assembler import LegacyIncomeStatementAssembler

import datetime

class IncomeStatementAssembler():
    def __init__(self):
        self.xbrl_assembler = XbrlIncomeStatementAssembler()
        self.legacy_assembler = LegacyIncomeStatementAssembler()

    def assemble(self, content, stock_symbol, date):
        # IFRS are available from 2013 to now
        if date >= datetime.date(2013, 1, 1):
            return self.xbrl_assembler.assemble(content, stock_symbol, date)
        # Otherwise we use legacy data
        else:
            return self.legacy_assembler.assemble(content, stock_symbol, date)
