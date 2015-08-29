#-*- coding: utf-8 -*-

from stockcat.common.json_utils import JsonUtils

import datetime
import unittest

class JsonUtilsTest(unittest.TestCase):
    def setUp(self):
        self.json_utils = JsonUtils()

    def tearDown(self):
        self.json_utils = None

    def test_load(self):
        path = './stockcat/tests/unit/data/json/memento.json'
        actual = self.json_utils.load(path)

        self.assertEqual(actual['state'], { 'value' : 'spider', 'type' : 'str' })

        self.assertEqual(actual['all_entry_list']['type'], 'list')
        self.assertEqual(len(actual['all_entry_list']['value']), 1)
        actual_date = actual['all_entry_list']['value'][0]['date']
        expected_date = { 'value' : '2010-12-31', 'type' : 'datetime.date' }
        self.assertEqual(actual_date, expected_date)
        actual_date = actual['all_entry_list']['value'][0]['stock_symbol']
        expected_date = { 'value' : '2330', 'type' : 'str' }
        self.assertEqual(actual_date, expected_date)

    def test_filter_key_list(self):
        json = {
            'state' : 'spider',
            'all_entry_list' : [
                { 
                    'stock_symbol' : '2330',
                    'date' : datetime.date(2010, 12, 31)
                },
            ],
        }
        actual = self.json_utils.filter_key_list(json, ['state'])
        self.assertEqual(actual, { 'state' : 'spider' })

    def test_add_type(self):
        json = {
            'state' : 'spider',
            'all_entry_list' : [
                { 
                    'stock_symbol' : '2330',
                    'date' : datetime.date(2010, 12, 31)
                },
            ],
        }
        actual = self.json_utils.add_type(json)

        self.assertEqual(actual['state'], { 'value' : 'spider', 'type' : 'str' })

        self.assertEqual(actual['all_entry_list']['type'], 'list')
        self.assertEqual(len(actual['all_entry_list']['value']), 1)
        actual_date = actual['all_entry_list']['value'][0]['date']
        expected_date = { 'value' : '2010-12-31', 'type' : 'datetime.date' }
        self.assertEqual(actual_date, expected_date)
        actual_date = actual['all_entry_list']['value'][0]['stock_symbol']
        expected_date = { 'value' : '2330', 'type' : 'str' }
        self.assertEqual(actual_date, expected_date)

    def test_remove_type(self):
        json = {
            'state' : {
                'type' : 'str', 
                'value' : 'spider'
            }, 
            'all_entry_list' : {
                'type' : 'list', 
                'value' : [
                    {
                        'date' : {
                            'type' : 'datetime.date', 
                            'value' : '2010-12-31'
                        }, 
                        'stock_symbol' : {
                            'type' : 'str', 
                            'value' : '2330'
                        }
                    }
                ]
            }, 
        }
        actual = self.json_utils.remove_type(json)

        self.assertEqual(actual['state'], 'spider')
        
        expected = [{ 'stock_symbol' : '2330', 'date' : datetime.date(2010, 12, 31) }]
        self.assertEqual(actual['all_entry_list'], expected)
