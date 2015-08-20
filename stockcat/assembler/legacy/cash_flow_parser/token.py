#-*- coding: utf-8 -*-

class Token():
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def get_token_type(self):
        return self.token_type

    def get_value(self):
        return self.value