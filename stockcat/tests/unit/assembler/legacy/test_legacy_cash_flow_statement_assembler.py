#-*- coding: utf-8 -*-

from stockcat.assembler.legacy.legacy_cash_flow_statement_assembler import LegacyCashFlowStatementAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class LegacyCashFlowStatementAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = LegacyCashFlowStatementAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None

    def test_assemble_2330(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st39?encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=false&co_id=2330&year=99&season=03
        content = self.file_utils.read_file('./stockcat/tests/unit/data/legacy_cash_flow_statement/2330/2010/03.html')
        column_name_list, row_list = self.assembler.assemble(content)
        self.assertEqual(column_name_list, [u'會計科目', datetime.date(2010, 9, 30), datetime.date(2009, 9, 30)])
        self.assertEqual(row_list[0], [])
        self.assertEqual(row_list[1], [(u'營業活動之現金流量', 0)])
        self.assertEqual(row_list[2], [(u'歸屬予母公司股東之淨利', 2), 120884560, 56551787])
        self.assertEqual(row_list[3], [(u'歸屬予少數股權之淨利', 2), 530446, 54024])
        self.assertEqual(row_list[35], [])
        self.assertEqual(row_list[36], [(u'營業活動之淨現金流入', 4), 158911867, 97967044])
        self.assertEqual(row_list[37], [])
        self.assertEqual(row_list[51], [])
        self.assertEqual(row_list[52], [(u'投資活動之淨現金流出', 4), -155529046, -49366789])
        self.assertEqual(row_list[53], [])
        self.assertEqual(row_list[65], [])
        self.assertEqual(row_list[66], [(u'融資活動之淨現金流出', 4), -41335338, -85193851])
        self.assertEqual(row_list[67], [])
