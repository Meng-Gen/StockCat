#-*- coding: utf-8 -*-

from stockcat.common.date_utils import DateUtils

class OperatingRevenueSummaryFeed():
    def __init__(self):
        self.date_utils = DateUtils()

    def get(self, dao):
        feed = []
        stmt_date = self.date_utils.get_last_date_of_month(dao.get_stmt_date())
        release_date = dao.get_release_date()
        for row in dao.get_row_list():
            stock_symbol = row[0]
            this_month_value = row[2]
            last_month_value = row[3]
            entry = {
                'release_date' : release_date,
                'stock_symbol' : stock_symbol,
                'stmt_date' : stmt_date, 
                'account' : u'當月營收',
                'account_order' : 1,
                'value' : this_month_value
            }
            feed.append(entry)
            entry = {
                'release_date' : release_date,
                'stock_symbol' : stock_symbol,
                'stmt_date' : self.date_utils.get_last_date_of_prev_month(stmt_date), 
                'account' : u'上月營收',
                'account_order' : 2,
                'value' : last_month_value
            }
            feed.append(entry)
        return tuple(feed)
