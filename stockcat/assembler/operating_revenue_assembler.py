#-*- coding: utf-8 -*-

from stockcat.assembler.ifrs.ifrs_operating_revenue_assembler import IfrsOperatingRevenueAssembler
from stockcat.assembler.legacy.legacy_operating_revenue_assembler import LegacyOperatingRevenueAssembler

import datetime

class OperatingRevenueAssembler():
    def __init__(self):
        self.ifrs_assembler = IfrsOperatingRevenueAssembler()
        self.legacy_assembler = LegacyOperatingRevenueAssembler()

    def assemble(self, content, stock_symbol, date):
        # IFRS are available from 2013 to now
        if date >= datetime.date(2013, 1, 1):
            return self.ifrs_assembler.assemble(content, stock_symbol, date)
        # Otherwise we use legacy data
        else:
            return self.legacy_assembler.assemble(content, stock_symbol, date)
