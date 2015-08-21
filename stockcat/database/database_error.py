#-*- coding: utf-8 -*-

class DatabaseError(Exception):
    def __init__(self, param):
        self.param = param

class NoTableDatabaseError(DatabaseError):
    def __str__(self):
        return '''NoTableDatabaseError on [{param}]'''.format(param=self.param)

class NoEntryDatabaseError(DatabaseError):
    def __str__(self):
        return '''NoEntryDatabaseError on [{param}]'''.format(param=self.param)
