#-*- coding: utf-8 -*-

from stockcat.database.database_error import NoTableDatabaseError
from stockcat.database.database_error import NoEntryDatabaseError

import psycopg2

class PostgresDatabaseHealthChecker():
    def __init__(self, connection_string="dbname='stockcat' user='stockcat' host='localhost' password='stockcat'"):
        self.connection_string = connection_string

    def check_connection(self):
        connection = psycopg2.connect(self.connection_string)
        connection.close()

    def check_table_existed(self, table):
        # fetch table names
        connection = psycopg2.connect(self.connection_string)
        cursor = connection.cursor()
        cursor.execute("select tablename from pg_tables where schemaname='public'")
        records = cursor.fetchall()
        cursor.close()
        connection.close()

        # flatten to string list
        tables = [record[0] for record in records]
        if table not in tables:
            raise NoTableDatabaseError({'table' : table})

    def check_entry_existed(self, entry):
        # build operation
        operation = self.__build_operation(entry)

        # pass table name as a parameter
        as_is_entry = entry.copy()
        as_is_entry['table'] = psycopg2.extensions.AsIs(entry['table'])

        connection = psycopg2.connect(self.connection_string)
        cursor = connection.cursor()
        cursor.execute(operation, as_is_entry)
        record_count, = cursor.fetchone()
        cursor.close()
        connection.close()

        if record_count == 0:
            raise NoEntryDatabaseError(entry)

    def __build_operation(self, entry):
        keys = entry.keys()
        keys.sort()
        if keys == ['stmt_date', 'stock_symbol', 'table']:
            return u"select count(1) from %(table)s where stock_symbol = %(stock_symbol)s and stmt_date = %(stmt_date)s"
        elif keys == ['stock_symbol', 'table']:
            return u"select count(1) from %(table)s where stock_symbol = %(stock_symbol)s"
        else:
            raise ValueError
