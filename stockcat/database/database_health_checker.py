#-*- coding: utf-8 -*-

import psycopg2

class DatabaseHealthChecker():
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def check_connection(self):
        connection = psycopg2.connect(self.connection_string)

    def check_table_existed(self, table_name):
        # fetch table names
        connection = psycopg2.connect(self.connection_string)
        cursor = connection.cursor()
        cursor.execute("select tablename from pg_tables where schemaname='public'")
        records = cursor.fetchall()
        connection.close()

        # flatten to string list
        table_names = [record[0] for record in records]
        if table_name not in table_names:
            raise ValueError
