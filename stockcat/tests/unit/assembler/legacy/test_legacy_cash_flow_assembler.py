#-*- coding: utf-8 -*-

from stockcat.assembler.legacy.legacy_cash_flow_assembler import LegacyCashFlowAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class LegacyCashFlowAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = LegacyCashFlowAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None

    def test_assemble_2330_in_2010Q3(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st39?encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=false&co_id=2330&year=99&season=03
        content = self.file_utils.read_file('./stockcat/tests/unit/data/legacy_cash_flow/2330/2010/03.html')
        dao = self.assembler.assemble(content, '2330', datetime.date(2010, 9, 30))
        
        column_name_list = dao.get_column_name_list()
        row_list = dao.get_row_list()
        
        self.assertEqual(column_name_list, [u'會計科目', datetime.date(2010, 9, 30), datetime.date(2009, 9, 30)])
        self.assertEqual(row_list[0], [u'營業活動之現金流量：'])
        self.assertEqual(row_list[1], [u'歸屬予母公司股東之淨利', 120884560, 56551787])
        self.assertEqual(row_list[2], [u'歸屬予少數股權之淨利', 530446, 54024])
        self.assertEqual(row_list[34], [u'營業活動之淨現金流入', 158911867, 97967044])
        self.assertEqual(row_list[48], [u'投資活動之淨現金流出', -155529046, -49366789])
        self.assertEqual(row_list[60], [u'融資活動之淨現金流出', -41335338, -85193851])

    def test_assemble_2330_in_2011Q1(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st39?encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=false&co_id=2330&year=100&season=01
        content = self.file_utils.read_file('./stockcat/tests/unit/data/legacy_cash_flow/2330/2011/01.html')
        dao = self.assembler.assemble(content, '2330', datetime.date(2011, 3, 31))
        
        column_name_list = dao.get_column_name_list()
        row_list = dao.get_row_list()

        self.assertEqual(column_name_list, [u'會計科目', datetime.date(2011, 3, 31), datetime.date(2010, 3, 31)])
        self.assertEqual(row_list[0], [u'營業活動之現金流量-間接法'])
        self.assertEqual(row_list[1], [u'合併總(損)益', 36427092, 33825315])

    def test_assemble_2330_in_2011Q2(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st39?encodeURIComponent=1&step=1&firstin=1&off=1&keyword4=&code1=&TYPEK2=&checkbtn=&queryName=co_id&TYPEK=all&isnew=false&co_id=2330&year=100&season=02
        content = self.file_utils.read_file('./stockcat/tests/unit/data/legacy_cash_flow/2330/2011/02.html')
        dao = self.assembler.assemble(content, '2330', datetime.date(2011, 6, 30))
        
        column_name_list = dao.get_column_name_list()
        row_list = dao.get_row_list()

        self.assertEqual(column_name_list, [u'會計科目', datetime.date(2011, 6, 30), datetime.date(2010, 6, 30)])
        self.assertEqual(row_list[0], [u'營業活動之現金流量-間接法'])
        self.assertEqual(row_list[1], [u'合併總(損)益', 72455291, 74291550])
        self.assertEqual(row_list[29], [u'營業活動之淨現金流入(流出)', 119541434, 94959938])
        self.assertEqual(row_list[44], [u'投資活動之淨現金流入(流出)', -116023709, -110497580])
        self.assertEqual(row_list[52], [u'融資活動之淨現金流入(流出)', 1876424, 16772654])
