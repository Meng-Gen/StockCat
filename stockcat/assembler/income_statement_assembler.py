#-*- coding: utf-8 -*-

from stockcat.assembler.xbrl.xbrl_income_statement_assembler import XbrlIncomeStatementAssembler
from stockcat.assembler.legacy.legacy_income_statement_assembler import LegacyIncomeStatementAssembler

import datetime

class IncomeStatementAssembler():
    def __init__(self):
        self.xbrl_assembler = XbrlIncomeStatementAssembler()
        self.legacy_assembler = LegacyIncomeStatementAssembler()
        # IFRS are available after year 2013. Legacy are available before year 2013. 
        self.splitted_date = datetime.date(2013, 1, 1)

    def assemble(self, param):
        if param['date'] >= self.splitted_date:
            return self.xbrl_assembler.assemble(param)
        else:
            return self.legacy_assembler.assemble(param)
