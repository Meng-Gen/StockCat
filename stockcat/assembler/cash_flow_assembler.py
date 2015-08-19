#-*- coding: utf-8 -*-

from stockcat.assembler.xbrl.xbrl_cash_flow_assembler import XbrlCashFlowAssembler
from stockcat.assembler.legacy.legacy_cash_flow_assembler import LegacyCashFlowAssembler

import datetime

class CashFlowAssembler():
    def __init__(self):
        self.xbrl_assembler = XbrlCashFlowAssembler()
        self.legacy_assembler = LegacyCashFlowAssembler()

    def assemble(self, content, stock_symbol, date):
        # IFRS are available from 2013 to now
        if date >= datetime.date(2013, 1, 1):
            return self.xbrl_assembler.assemble(content, stock_symbol, date)
        # Otherwise we use legacy data
        else:
            return self.legacy_assembler.assemble(content, stock_symbol, date)
