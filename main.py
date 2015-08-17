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

def assemble_legacy_cash_flow_statement():
    from stockcat.assembler.legacy.legacy_cash_flow_statement_assembler import LegacyCashFlowStatementAssembler
    from stockcat.common.file_utils import FileUtils
    assembler = LegacyCashFlowStatementAssembler()
    file_utils = FileUtils()
    content = file_utils.read_file('./stockcat/tests/unit/data/legacy_cash_flow_statement/2330/2010/03.html')
    column_name_list, row_list = assembler.assemble(content)

def check_postgres_database():
    from stockcat.database.postgres_database_health_checker import PostgresDatabaseHealthChecker
    connection_string = "dbname='stockcat' user='stockcat' host='localhost' password='stockcat'"
    checker = PostgresDatabaseHealthChecker(connection_string)
    checker.check_connection()
    checker.check_table_existed('operating_revenue')

def run_operating_revenue_pipeline():
    from stockcat.pipeline.operating_revenue_pipeline import OperatingRevenuePipeline
    pipeline = OperatingRevenuePipeline()
    pipeline.run('2330', datetime.date(2010, 1, 1))

def run_many_operating_revenue_pipeline():
    from stockcat.pipeline.operating_revenue_pipeline import OperatingRevenuePipeline
    pipeline = OperatingRevenuePipeline()
    date_period = datetime.date(2010, 1, 1), datetime.date(2015, 8, 10)
    # may take a lot of time
    pipeline.run_many('2330', date_period, ['spider', 'assembler', 'database'])
    pipeline.run_many('2330', date_period)

def run_stock_symbol_pipeline():
    from stockcat.pipeline.stock_symbol_pipeline import StockSymbolPipeline
    pipeline = StockSymbolPipeline()
    pipeline.run()

def analyze_stock_symbol():
    from stockcat.analyzer.stock_symbol_analyzer import StockSymbolAnalyzer
    analyzer = StockSymbolAnalyzer()
    stock_symbol_list = analyzer.analyze()
    print stock_symbol_list[:10]

def get_database():
    from stockcat.database.database import Database
    database = Database()
    stock_symbol_list = database.get_stock_symbol()
    print stock_symbol_list[:10]

def crawl_operating_revenue_summary():
    from stockcat.spider.operating_revenue_summary_spider import OperatingRevenueSummarySpider
    spider = OperatingRevenueSummarySpider()
    spider.crawl('stock_exchange_market', datetime.date(2015, 1, 31))

def run_operating_revenue_summary_pipeline():
    from stockcat.pipeline.operating_revenue_summary_pipeline import OperatingRevenueSummaryPipeline
    pipeline = OperatingRevenueSummaryPipeline()
    date_period = datetime.date(2015, 8, 1), datetime.date(2015, 8, 10)
    pipeline.run_many(date_period)

def crawl_capital_increase_history():
    from stockcat.spider.capital_increase_history_spider import CapitalIncreaseHistorySpider
    spider = CapitalIncreaseHistorySpider()
    spider.crawl('2498')

def assemble_capital_increase_history():
    from stockcat.assembler.capital_increase_history_assembler import CapitalIncreaseHistoryAssembler
    from stockcat.common.file_utils import FileUtils
    assembler = CapitalIncreaseHistoryAssembler()
    file_utils = FileUtils()
    content = file_utils.read_file('./stockcat/tests/unit/data/capital_increase_history/2498.html')
    assembler.assemble(content, '2498')

def run_capital_increase_history_pipeline():
    from stockcat.pipeline.capital_increase_history_pipeline import CapitalIncreaseHistoryPipeline
    pipeline = CapitalIncreaseHistoryPipeline()
    pipeline.run('2498', ['spider', 'assembler', 'database'])

def main():
    run_capital_increase_history_pipeline()

if __name__ == '__main__':
    sys.exit(main())