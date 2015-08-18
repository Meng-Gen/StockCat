#-*- coding: utf-8 -*-

class StockSymbolFeed():
    def get(self, dao):
        feed = []
        release_date = dao.get_release_date()
        for stock_symbol, stock_name, isin_code, listing_date, market_category, industry_category, cfi_code, comment in dao.get_row_list():
            entry = {
                'stock_symbol' : stock_symbol,
                'release_date' : release_date, 
                'stock_name' : stock_name,
                'isin_code' : isin_code,
                'listing_date' : listing_date,
                'market_category' : market_category,
                'industry_category' : industry_category,
                'cfi_code' : cfi_code,
            }
            feed.append(entry)
        return tuple(feed)
