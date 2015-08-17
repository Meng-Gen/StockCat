#-*- coding: utf-8 -*-

class AssembleError(Exception):
    def __init__(self, param):
        self.param = param

class NoRecordAssembleError(AssembleError):
    def __str__(self):
        return '''NoRecordAssembleError on [{param}]'''.format(param=self.param)

class OverQueryAssembleError(AssembleError):
    def __str__(self):
        return '''OverQueryAssembleError on [{param}]'''.format(param=self.param)

class PrivateRecordAssembleError(AssembleError):
    def __str__(self):
        return '''PrivateRecordAssembleError on [{param}]'''.format(param=self.param)
