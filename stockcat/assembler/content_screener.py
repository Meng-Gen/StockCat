#-*- coding: utf-8 -*-

from stockcat.assembler.assemble_error import NoPublishAssembleError
from stockcat.assembler.assemble_error import NoRecordAssembleError
from stockcat.assembler.assemble_error import OverQueryAssembleError

class ContentScreener():
    def screen(self, content, stock_symbol, date):
        decoded = content.decode('utf-8')
        if u'查詢過於頻繁，請於稍後再查詢' in decoded:
            raise OverQueryAssembleError(stock_symbol, date)
        if u'未公告合併營業收入(採自願公告制)' in decoded:
            raise NoPublishAssembleError(stock_symbol, date)
        if u'資料庫中查無需求資料' in decoded:
            raise NoRecordAssembleError(stock_symbol, date)
