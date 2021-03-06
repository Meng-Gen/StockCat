#-*- coding: utf-8 -*-

from stockcat.assembler.assemble_error import NoRecordAssembleError
from stockcat.assembler.assemble_error import OverQueryAssembleError
from stockcat.assembler.assemble_error import PrivateRecordAssembleError
from stockcat.assembler.legacy.legacy_operating_revenue_assembler import LegacyOperatingRevenueAssembler
from stockcat.common.file_utils import FileUtils

import datetime
import unittest

class LegacyOperatingRevenueAssemblerTest(unittest.TestCase):
    def setUp(self):
        self.assembler = LegacyOperatingRevenueAssembler()
        self.file_utils = FileUtils()

    def tearDown(self):
        self.assembler = None
        self.file_utils = None
    
    def test_assemble_2330(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st10?encodeURIComponent=1&run=Y&step=0&colorchg=&TYPEK=sii%20&co_id=2330&off=1&year=99&month=09&firstin=true
        path = './stockcat/tests/unit/data/legacy_operating_revenue/2330/2010/09.html'
        param = {
            'content' : self.file_utils.read_file(path),
            'stock_symbol' : '2330',
            'date' : datetime.date(2010, 9, 30)
        }
        dao = self.assembler.assemble(param)

        self.assertEqual(dao.get_column_name_list(), [u'項目', datetime.date(2010, 9, 30)])
        self.assertEqual(dao.get_stock_symbol(), param['stock_symbol'])
        self.assertEqual(dao.get_date(), param['date'])

        row_list = dao.get_row_list()
        self.assertEqual(row_list[0], [u'本月', 37637898])
        self.assertEqual(row_list[1], [u'去年同期', 28936225])
        self.assertEqual(row_list[2], [u'增減金額', 8701673])
        self.assertEqual(row_list[3], [u'增減百分比', 30.07])
        self.assertEqual(row_list[4], [u'本年累計', 309395679])
        self.assertEqual(row_list[5], [u'去年累計', 203647791])
        self.assertEqual(row_list[6], [u'增減金額', 105747888])
        self.assertEqual(row_list[7], [u'增減百分比', 51.93])
    
    def test_assemble_raise_private_record_assemble_error(self):
        # online: http://mops.twse.com.tw/mops/web/ajax_t05st10?encodeURIComponent=1&run=Y&step=0&colorchg=&TYPEK=sii%20&co_id=1101&off=1&year=99&month=09&firstin=true
        path = './stockcat/tests/unit/data/legacy_operating_revenue/1101/2010/09.html'
        param = {
            'content' : self.file_utils.read_file(path),
            'stock_symbol' : '1101',
            'date' : datetime.date(2010, 9, 30)
        }
        with self.assertRaises(PrivateRecordAssembleError) as context:
            self.assembler.assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])
        self.assertEqual(context.exception.param['date'], param['date'])

    def test_assemble_raise_over_query_assemble_error(self):
        path = './stockcat/tests/unit/data/error/too_much_query_error.html'
        param = {
            'content' : self.file_utils.read_file(path),
            'stock_symbol' : '2330',
            'date' : datetime.date(2010, 9, 30)
        }
        with self.assertRaises(OverQueryAssembleError) as context:
            self.assembler.assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])
        self.assertEqual(context.exception.param['date'], param['date'])

    def test_assemble_raise_no_record_assemble_error(self):
        path = './stockcat/tests/unit/data/error/no_record_error.html'
        param = {
            'content' : self.file_utils.read_file(path),
            'stock_symbol' : '2330',
            'date' : datetime.date(2010, 9, 30)
        }
        with self.assertRaises(NoRecordAssembleError) as context:
            self.assembler.assemble(param)
        self.assertEqual(context.exception.param['stock_symbol'], param['stock_symbol'])
        self.assertEqual(context.exception.param['date'], param['date'])
