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
            if self.account_synonym.get(account) == u'當月營收':
                entry = {
                    'release_date' : release_date,
                    'stock_symbol' : stock_symbol,
                    'stmt_date' : self.date_utils.get_last_date_of_month(release_date), 
                    'account' : u'當月營收',
                    'account_order' : 1,
                    'value' : value
                }
                feed.append(entry)
        return tuple(feed)
