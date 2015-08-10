#-*- coding: utf-8 -*-

from stockcat.common.date_utils import DateUtils
from stockcat.dao.operating_revenue_dao import OperatingRevenueDao
from stockcat.synonym.account_synonym import AccountSynonym

class OperatingRevenueFeed():
    def __init__(self):
        self.account_synonym = AccountSynonym()
        self.date_utils = DateUtils()

    def get(self, dao):
        feed = []
        release_date = self.date_utils.get_last_date_of_month(dao.get_date())
        stock_symbol = dao.get_stock_symbol()
        for account, value in dao.get_row_list():
            if self.account_synonym.get(account) == u'本月':
                entry = {
                    'release_date' : release_date,
                    'stock_symbol' : stock_symbol,
                    'stmt_date' : self.date_utils.get_last_date_of_month(release_date), 
                    'account' : u'本月',
                    'account_order' : 1,
                    'value' : value
                }
                feed.append(entry)
            elif self.account_synonym.get(account) == u'去年同期':
                entry = {
                    'release_date' : release_date,
                    'stock_symbol' : stock_symbol,
                    'stmt_date' : self.date_utils.get_last_date_of_prev_month(release_date), 
                    'account' : u'去年同期',
                    'account_order' : 2,
                    'value' : value
                }
                feed.append(entry)
        return tuple(feed)
