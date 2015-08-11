#-*- coding: utf-8 -*-

class AssembleError(Exception):
    def __init__(self, stock_symbol, date):
        self.stock_symbol = stock_symbol
        self.date = date

class OverQueryAssembleError(AssembleError):
    def __str__(self):
        return '''Query too much while [{stock_symbol}] on [{date}]'''.format(stock_symbol=self.stock_symbol, date=self.date)

class NoPublishAssembleError(AssembleError):
    def __str__(self):
        return '''[{stock_symbol}] does not publish statement on [{date}]'''.format(stock_symbol=self.stock_symbol, date=self.date)

class NoRecordAssembleError(AssembleError):
    def __str__(self):
        return '''[{stock_symbol}] does not have statement on [{date}]'''.format(stock_symbol=self.stock_symbol, date=self.date)
