#-*- coding: utf-8 -*-

import psycopg2

class PostgresDatabaseHealthChecker():
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def check_connection(self):
        connection = psycopg2.connect(self.connection_string)

    def check_table_existed(self, table):
        # fetch table names
        connection = psycopg2.connect(self.connection_string)
        cursor = connection.cursor()
        cursor.execute("select tablename from pg_tables where schemaname='public'")
        records = cursor.fetchall()
        connection.close()

        # flatten to string list
        tables = [record[0] for record in records]
        if table not in tables:
            raise ValueError
