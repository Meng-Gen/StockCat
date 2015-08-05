#-*- coding: utf-8 -*-

from stockcat.feed.stock_symbol.stock_exchange_market_feed import StockExchangeMarketFeed
from stockcat.feed.stock_symbol.otc_market_feed import OtcMarketFeed

class StockSymbolFeed():
    def get(self):
        StockExchangeMarketFeed().get()
        #OtcMarketFeed().get()
