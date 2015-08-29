#-*- coding: utf-8 -*-

from stockcat.assembler.xbrl.xbrl_cash_flow_assembler import XbrlCashFlowAssembler
from stockcat.assembler.legacy.legacy_cash_flow_assembler import LegacyCashFlowAssembler

import datetime

class CashFlowAssembler():
    def __init__(self):
        self.xbrl_assembler = XbrlCashFlowAssembler()
        self.legacy_assembler = LegacyCashFlowAssembler()
        # IFRS are available after year 2013. Legacy are available before year 2013. 
        self.splitted_date = datetime.date(2013, 1, 1)

    def assemble(self, param):
        if param['date'] >= self.splitted_date:
            return self.xbrl_assembler.assemble(param)
        else:
            return self.legacy_assembler.assemble(param)
