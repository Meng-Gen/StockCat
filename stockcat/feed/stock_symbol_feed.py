#-*- coding: utf-8 -*-

from stockcat.dao.stock_symbol_dao import StockSymbolDao

class StockSymbolFeed():
    def get(self, dao):
        feed = []
        for stock_symbol, stock_name, isin_code, listing_date, market_category, industry_category, cfi_code, comment in dao.get_row_list():
            entry = {
                'stock_symbol' : stock_symbol,
                'stock_name' : stock_name,
                'isin_code' : isin_code,
                'listing_date' : listing_date,
                'market_category' : market_category,
                'industry_category' : industry_category,
                'cfi_code' : cfi_code,
            }
            feed.append(entry)
        return tuple(feed)
