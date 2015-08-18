#-*- coding: utf-8 -*-

from stockcat.database.postgres_database_health_checker import PostgresDatabaseHealthChecker

import datetime
import unittest

class PostgresDatabaseTest(unittest.TestCase):
    def setUp(self):
        self.checker = PostgresDatabaseHealthChecker("dbname='stockcat' user='stockcat' host='localhost' password='stockcat'")

    def tearDown(self):
        self.checker = None
    
    def test_check_connection(self):
        self.checker.check_connection()

    def test_check_table_existed(self):
        self.checker.check_table_existed('operating_revenue')
