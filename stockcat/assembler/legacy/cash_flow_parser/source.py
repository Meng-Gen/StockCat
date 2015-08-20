#-*- coding: utf-8 -*-

class Source():
    def __init__(self, source):
        self.source = source
        self.source_size = len(source)
        self.pos = -1
        self.c0 = None

    def get_current_char(self):
        return self.c0

    def advance(self):
        self.pos += 1
        if self.pos < self.source_size:
            self.c0 = self.source[self.pos]
        else:
            self.c0 = None

    def push_back(self):
        self.pos -= 1
        if self.pos >= 0:
            self.c0 = self.source[self.pos]
        else:
            self.c0 = None
