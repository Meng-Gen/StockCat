#-*- coding: utf-8 -*-

from stockcat.assembler.legacy.cash_flow_parser.token import Token
from stockcat.common.string_utils import StringUtils

class Scanner():
    def __init__(self, source):
        self.source = source
        self.c0 = None
        self.buffer = []
        self.tokens = []
        self.curr_token_pos = 0
        self.string_utils = StringUtils()

    def scan(self):
        while True:
            self.__advance()
            if self.c0 == '\n':
                self.tokens.append(Token('TK_EOL'))
            elif self.c0 == '-':
                # - -- -number
                self.__advance()
                if self.c0 == '-':
                    self.__scan_seperation()
                elif self.__is_decimal_digit(self.c0):
                    self.buffer.append('-')
                    self.__scan_number()
                else:
                    self.tokens.append(Token('TK_NUMBER', '-'))
                    self.__push_back()
            elif self.c0 == '=':
                # = ==
                self.__advance()
                if self.c0 == '=':
                    self.__scan_seperation()
                else:
                    self.tokens.append(Token('TK_EQUALS'))
                    self.__push_back()
            elif self.c0 == '(':
                self.tokens.append(Token('TK_LEFT_PAREN'))
            elif self.c0 == ')':
                self.tokens.append(Token('TK_RIGHT_PAREN'))
            elif self.__is_chinese_alpha(self.c0):
                self.__scan_account()
            elif self.__is_decimal_digit(self.c0):
                self.__scan_number_or_account()
            if not self.c0:
                break
        self.tokens.append(Token('TK_EOS'))

    def get_tokens(self):
        return self.tokens

    def __scan_seperation(self):
        while True:
            self.__advance()
            if self.c0 == '\n' or self.c0 is None:
                self.__push_back()
                break
        self.tokens.append(Token('TK_SEPERATION'))

    def __scan_account(self):
        self.buffer.append(self.c0)
        while True:
            self.__advance()
            if self.c0 == '\n' or self.c0 == ' ' or self.c0 is None:
                self.__push_back()
                break
            self.buffer.append(self.c0)
        self.tokens.append(Token('TK_ACCOUNT', ''.join(self.buffer)))
        self.__reset_buffer()

    def __scan_number_or_account(self):
        token_type = 'TK_NUMBER'
        self.buffer.append(self.c0)
        while True:
            self.__advance()
            if self.c0 == '\n' or self.c0 == ' ' or self.c0 == ')' or self.c0 is None:
                self.__push_back()
                break
            if self.__is_chinese_alpha(self.c0):
                token_type = 'TK_ACCOUNT'
            self.buffer.append(self.c0)
        self.tokens.append(Token(token_type, ''.join(self.buffer)))
        self.__reset_buffer()

    def __is_chinese_alpha(self, c):
        if c >= u'\u4e00' and c <= u'\u9fff':
            return True
        if c >= u'\u3400' and c <= u'\u4dff':
            return True
        if c >= u'\uf900' and c <= u'\ufaff':
            return True
        return False

    def __is_decimal_digit(self, c):
        return c >= u'0' and c <= u'9'

    def __advance(self):
        self.source.advance()
        self.c0 = self.source.get_current_char()

    def __push_back(self):
        self.source.push_back()
        self.c0 = self.source.get_current_char()

    def __reset_buffer(self):
        self.buffer = []