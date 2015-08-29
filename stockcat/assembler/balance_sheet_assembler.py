#-*- coding: utf-8 -*-

from stockcat.assembler.xbrl.xbrl_balance_sheet_assembler import XbrlBalanceSheetAssembler
from stockcat.assembler.legacy.legacy_balance_sheet_assembler import LegacyBalanceSheetAssembler

import datetime

class BalanceSheetAssembler():
    def __init__(self):
        self.xbrl_assembler = XbrlBalanceSheetAssembler()
        self.legacy_assembler = LegacyBalanceSheetAssembler()
        # IFRS are available after year 2013. Legacy are available before year 2013. 
        self.splitted_date = datetime.date(2013, 1, 1)

    def assemble(self, param):
        if param['date'] >= self.splitted_date:
            return self.xbrl_assembler.assemble(param)
        else:
            return self.legacy_assembler.assemble(param)
