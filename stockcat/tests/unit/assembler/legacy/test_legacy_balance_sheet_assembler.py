#-*- coding: utf-8 -*-

from stockcat.assembler.legacy.legacy_balance_sheet_assembler import LegacyBalanceSheetAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class LegacyBalanceSheetAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = LegacyBalanceSheetAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None

    def test_assemble_2330(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st33?encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=false&co_id=2330&year=99&season=03
        content = self.file_utils.read_file('./stockcat/tests/unit/data/legacy_balance_sheet/2330/2010/03.html')
        dao = self.assembler.assemble(content, '2330', datetime.date(2010, 9, 30))
        
        column_name_list = dao.get_column_name_list()
        row_list = dao.get_row_list()
        
        self.assertEqual(column_name_list, [u'會計科目', datetime.date(2010, 9, 30), datetime.date(2009, 9, 30)])
        self.assertEqual(row_list[0], [(u'資產', 8)])
        self.assertEqual(row_list[1], [(u'流動資產', 8)])
        self.assertEqual(row_list[2], [(u'現金及約當現金', 10), 132268758, 156935077])
        self.assertEqual(row_list[6], [(u'應收帳款淨額', 10), 47370155, 35879778])
        self.assertEqual(row_list[10], [(u'存 貨', 10), 26663415, 19176052])
        self.assertEqual(row_list[12], [(u'流動資產', 12), 246637178, 244240939])
        self.assertEqual(row_list[13], [(u'基金及投資', 8)])
        self.assertEqual(row_list[19], [(u'基金及投資', 12), 39784245, 38553304])
        self.assertEqual(row_list[30], [(u'固定資產淨額', 12), 349179208, 236816024])
        self.assertEqual(row_list[40], [(u'資產總計', 12), 667552049, 541897118])
        self.assertEqual(row_list[41], [(u'負債及股東權益', 8)])
        self.assertEqual(row_list[42], [(u'負債', 8)])
        self.assertEqual(row_list[43], [(u'流動負債', 8)])
        self.assertEqual(row_list[53], [(u'流動負債', 12), 109235939, 55008722])
        self.assertEqual(row_list[54], [(u'長期負債', 8)])
        self.assertEqual(row_list[58], [(u'長期負債', 12), 12397877, 14967865])
        self.assertEqual(row_list[65], [(u'負債總計', 12), 126647972, 75270447])
        self.assertEqual(row_list[66], [(u'股東權益', 8)])
        self.assertEqual(row_list[67], [(u'股本', 8)])
        self.assertEqual(row_list[68], [(u'普通股股本', 10), 259073440, 259006623])
        self.assertEqual(row_list[69], [(u'資本公積', 8)])
        self.assertEqual(row_list[70], [(u'資本公積合計', 12), 55634070, 55439919])
        self.assertEqual(row_list[71], [(u'保留盈餘', 8)])
        self.assertEqual(row_list[75], [(u'保留盈餘合計', 12), 225059122, 149216633])
        self.assertEqual(row_list[81], [(u'股東權益總計', 10), 540904077, 466626671])
