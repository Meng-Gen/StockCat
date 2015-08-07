#-*- coding: utf-8 -*-

import datetime
import sys

def crawl_stock_symbol():
    from stockcat.spider.stock_symbol_spider import StockSymbolSpider
    spider = StockSymbolSpider()
    spider.crawl("stock_exchange_market")
    spider.crawl("otc_market")

def crawl_operating_revenue():
    from stockcat.spider.operating_revenue_spider import OperatingRevenueSpider
    spider = OperatingRevenueSpider()
    spider.crawl("2330", datetime.date(2010, 9, 30))
    spider.crawl("2330", datetime.date(2014, 9, 30))
    spider.crawl("1101", datetime.date(2010, 9, 30))
    spider.crawl("1101", datetime.date(2014, 9, 30))

def crawl_cash_flow_statement():
    from stockcat.spider.cash_flow_statement_spider import CashFlowStatementSpider
    spider = CashFlowStatementSpider()
    spider.crawl("2330", datetime.date(2010, 9, 30))
    spider.crawl("2330", datetime.date(2014, 9, 30))

def crawl_xbrl_financial_statement():
    from stockcat.spider.xbrl_financial_statement_spider import XbrlFinancialStatementSpider
    spider = XbrlFinancialStatementSpider()
    spider.crawl("2330", datetime.date(2010, 9, 30))
    spider.crawl("2330", datetime.date(2014, 9, 30))

def assemble_xbrl_balance_sheet():
    from stockcat.assembler.xbrl.xbrl_balance_sheet_assembler import XbrlBalanceSheetAssembler
    from stockcat.common.file_utils import FileUtils
    assembler = XbrlBalanceSheetAssembler()
    file_utils = FileUtils()
    content = file_utils.read_file('./stockcat/tests/unit/data/xbrl_financial_statement/2330/2014/03.html')
    column_name_list, row_list = assembler.assemble(content)

def assemble_legacy_income_statement():
    from stockcat.assembler.legacy.legacy_income_statement_assembler import LegacyIncomeStatementAssembler
    from stockcat.common.file_utils import FileUtils
    assembler = LegacyIncomeStatementAssembler()
    file_utils = FileUtils()
    content = file_utils.read_file('./stockcat/tests/unit/data/legacy_income_statement/2330/2010/03.html')
    column_name_list, row_list = assembler.assemble(content)

def assemble_legacy_balance_sheet():
    from stockcat.assembler.legacy.legacy_balance_sheet_assembler import LegacyBalanceSheetAssembler
    from stockcat.common.file_utils import FileUtils
    assembler = LegacyBalanceSheetAssembler()
    file_utils = FileUtils()
    content = file_utils.read_file('./stockcat/tests/unit/data/legacy_balance_sheet/2330/2010/03.html')
    column_name_list, row_list = assembler.assemble(content)

def main():
    assemble_legacy_balance_sheet()

if __name__ == '__main__':
    sys.exit(main())