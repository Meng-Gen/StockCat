#-*- coding: utf-8 -*-

from stockcat.feed.aries_feed import AriesFeed
from stockcat.common.date_utils import DateUtils

class CapitalIncreaseHistoryFeed(AriesFeed):
    pass

class CapitalIncreaseHistoryFeedBuilder():
    def __init__(self):
        self.date_utils = DateUtils()

    def build(self, dao):
        tuple_feed = self.__build_tuple(dao)
        return CapitalIncreaseHistoryFeed(tuple_feed)

    def __build_tuple(self, dao):
        feed = []
        stock_symbol = dao.get_stock_symbol()
        release_date = self.date_utils.now_date()
        for row in dao.get_row_list():
            stmt_date = row[0]
            capital_increase_by_cash = row[1]
            capital_increase_by_earnings = row[3]
            capital_increase_by_surplus = row[5]
            entry = {
                'release_date' : release_date,
                'stock_symbol' : stock_symbol,
                'stmt_date' : stmt_date, 
                'account' : u'現金增資',
                'account_order' : 1,
                'value' : capital_increase_by_cash
            }
            feed.append(entry)
            entry = {
                'release_date' : release_date,
                'stock_symbol' : stock_symbol,
                'stmt_date' : stmt_date, 
                'account' : u'盈餘轉增資',
                'account_order' : 2,
                'value' : capital_increase_by_earnings
            }
            feed.append(entry)
            entry = {
                'release_date' : release_date,
                'stock_symbol' : stock_symbol,
                'stmt_date' : stmt_date, 
                'account' : u'公積及其他',
                'account_order' : 3,
                'value' : capital_increase_by_surplus
            }
            feed.append(entry)    
        return tuple(feed)
