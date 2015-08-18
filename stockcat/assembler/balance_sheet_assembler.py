#-*- coding: utf-8 -*-

from stockcat.assembler.xbrl.xbrl_balance_sheet_assembler import XbrlBalanceSheetAssembler
from stockcat.assembler.legacy.legacy_balance_sheet_assembler import LegacyBalanceSheetAssembler

import datetime

class BalanceSheetAssembler():
    def __init__(self):
        self.xbrl_assembler = XbrlBalanceSheetAssembler()
        self.legacy_assembler = LegacyBalanceSheetAssembler()

    def assemble(self, content, stock_symbol, date):
        # IFRS are available from 2013 to now
        if date >= datetime.date(2013, 1, 1):
            return self.xbrl_assembler.assemble(content, stock_symbol, date)
        # Otherwise we use legacy data
        else:
            return self.legacy_assembler.assemble(content, stock_symbol, date)
