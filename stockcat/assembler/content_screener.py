#-*- coding: utf-8 -*-

from stockcat.assembler.assemble_error import NoRecordAssembleError
from stockcat.assembler.assemble_error import OverQueryAssembleError
from stockcat.assembler.assemble_error import PrivateRecordAssembleError

class ContentScreener():
    def screen(self, content, params):
        self.__screen_unicode(content, params)
        self.__screen_big5(content, params)

    def __screen_unicode(self, content, params):
        decoded = content.decode('utf-8', 'ignore')
        if u'查詢過於頻繁，請於稍後再查詢' in decoded:
            raise OverQueryAssembleError(params)
        if u'未公告合併營業收入(採自願公告制)' in decoded:
            raise PrivateRecordAssembleError(params)
        if u'資料庫中查無需求資料' in decoded:
            raise NoRecordAssembleError(params)
        if u'was not found on this server' in decoded:
            raise NoRecordAssembleError(params)

    def __screen_big5(self, content, params):
        decoded = content.decode('big5-hkscs', 'ignore')
        if 'stock_symbol' in params:
            if u'查無(%s)股本形成資料' % (params['stock_symbol']) in decoded:
                raise NoRecordAssembleError(params)
