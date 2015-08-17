#-*- coding: utf-8 -*-

from stockcat.assembler.assemble_error import NoRecordAssembleError
from stockcat.assembler.assemble_error import OverQueryAssembleError
from stockcat.assembler.assemble_error import PrivateRecordAssembleError

class ContentScreener():
    def screen(self, content, param):
        try:
            decoded = content.decode('utf-8')
            if u'查詢過於頻繁，請於稍後再查詢' in decoded:
                raise OverQueryAssembleError(param)
            if u'未公告合併營業收入(採自願公告制)' in decoded:
                raise PrivateRecordAssembleError(param)
            if u'資料庫中查無需求資料' in decoded:
                raise NoRecordAssembleError(param)
            if u'was not found on this server' in decoded:
                raise NoRecordAssembleError(param)
        except UnicodeDecodeError:
            pass