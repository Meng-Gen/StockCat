#-*- coding: utf-8 -*-

from stockcat.common.date_utils import DateUtils
from stockcat.dao.capital_increase_history_dao import CapitalIncreaseHistoryDao

class DividendPolicyFeed():
    def __init__(self):
        self.date_utils = DateUtils()

    def get(self, dao):
        feed = []
        stock_symbol = dao.get_stock_symbol()
        release_date = self.date_utils.now_date()
        for row in dao.get_row_list():
            stmt_date = row[0]
            cash_dividend = row[1] # 現金股利
            stock_dividend_from_retained_earnings = row[2] # 盈餘配股    
            stock_dividend_from_capital_reserve = row[3] # 公積配股
            employee_stock_bonuses_ratio = row[6] # 員工配股率%
            entry = {
                'release_date' : release_date,
                'stock_symbol' : stock_symbol,
                'stmt_date' : stmt_date, 
                'account' : u'現金股利',
                'account_order' : 1,
                'value' : cash_dividend
            }
            feed.append(entry)
            entry = {
                'release_date' : release_date,
                'stock_symbol' : stock_symbol,
                'stmt_date' : stmt_date, 
                'account' : u'盈餘配股',
                'account_order' : 2,
                'value' : stock_dividend_from_retained_earnings
            }
            feed.append(entry)
            entry = {
                'release_date' : release_date,
                'stock_symbol' : stock_symbol,
                'stmt_date' : stmt_date, 
                'account' : u'公積配股',
                'account_order' : 3,
                'value' : stock_dividend_from_capital_reserve
            }
            feed.append(entry) 
            entry = {
                'release_date' : release_date,
                'stock_symbol' : stock_symbol,
                'stmt_date' : stmt_date, 
                'account' : u'員工配股率',
                'account_order' : 4,
                'value' : employee_stock_bonuses_ratio
            }
            feed.append(entry) 
        return tuple(feed)
