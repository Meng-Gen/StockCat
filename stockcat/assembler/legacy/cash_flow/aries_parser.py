#-*- coding: utf-8 -*-

from stockcat.common.string_utils import StringUtils

import lxml.html

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

class Token():
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def get_token_type(self):
        return self.token_type

    def get_value(self):
        return self.value

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
                self.__scan_number()
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

    def __scan_number(self):
        self.buffer.append(self.c0)
        while True:
            self.__advance()
            if self.c0 == '\n' or self.c0 == ' ' or self.c0 == ')' or self.c0 is None:
                self.__push_back()
                break
            self.buffer.append(self.c0)
        self.tokens.append(Token('TK_NUMBER', ''.join(self.buffer)))
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

class AriesParser():
    def __init__(self, text):
        self.text = text
        self.head_splitted_account = None
        self.string_utils = StringUtils()

    def parse(self):
        lines = self.__scan_lines(self.text)
        return self.__parse_lines(lines)

    def __scan_lines(self, text):
        scanner = Scanner(Source(text))
        scanner.scan()
        tokens = scanner.get_tokens()

        lines = []
        tokens_in_line = []
        for token in tokens:
            tokens_in_line.append(token)
            if token.get_token_type() == 'TK_EOL':
                lines.append(tokens_in_line)
                tokens_in_line = []
        return lines

    def __parse_lines(self, lines):
        column_name_list = None
        visited_column_name_list = False
        row_list = []
        for line in lines:
            type_list = [token.get_token_type() for token in line]
            if type_list == ['TK_EOL']:
                continue
            elif type_list == ['TK_SEPERATION', 'TK_EOL']:
                continue
            elif type_list == ['TK_ACCOUNT', 'TK_ACCOUNT', 'TK_EOL']:
                column_name_list = self.__parse_column_name_list_line(line)
                visited_column_name_list = True
            elif visited_column_name_list:
                row = None
                if type_list == ['TK_ACCOUNT', 'TK_NUMBER', 'TK_NUMBER', 'TK_EOL']:
                    row = self.__parse_account_number_number_line(line)
                elif type_list == ['TK_ACCOUNT', 'TK_LEFT_PAREN', 'TK_NUMBER', 'TK_RIGHT_PAREN', 'TK_NUMBER', 'TK_EOL']:
                    row = self.__parse_account_paren_number_number_line(line)
                elif type_list == ['TK_ACCOUNT', 'TK_NUMBER', 'TK_LEFT_PAREN', 'TK_NUMBER', 'TK_RIGHT_PAREN', 'TK_EOL']:
                    row = self.__parse_account_number_paren_number_line(line)
                elif type_list == ['TK_ACCOUNT', 'TK_LEFT_PAREN', 'TK_NUMBER', 'TK_RIGHT_PAREN', 'TK_LEFT_PAREN', 'TK_NUMBER', 'TK_RIGHT_PAREN', 'TK_EOL']:
                    row = self.__parse_account_paren_number_paren_number_line(line)
                elif type_list == ['TK_ACCOUNT', 'TK_EOL']:
                    row = self.__parse_account_line(line)
                else:
                    raise ValueError
                row_list.append(row) if row else None
        return column_name_list, row_list

    # ['TK_ACCOUNT', 'TK_ACCOUNT', 'TK_EOL']
    def __parse_column_name_list_line(self, line):
        column_name_list = [u'會計科目']
        for i in [0, 1]:
            date_period = self.string_utils.from_local_string_to_date_period(line[i].get_value())
            stmt_date = date_period[1]
            column_name_list.append(stmt_date)  
        return column_name_list        

    # ['TK_ACCOUNT', 'TK_EOL']
    def __parse_account_line(self, line):
        return [line[0].get_value()]

    # ['TK_ACCOUNT', 'TK_NUMBER', 'TK_NUMBER', 'TK_EOL']
    def __parse_account_number_number_line(self, line):
        return [
            line[0].get_value(),
            self.string_utils.normalize_number(line[1].get_value()), 
            self.string_utils.normalize_number(line[2].get_value())
        ]

    # ['TK_ACCOUNT', 'TK_LEFT_PAREN', 'TK_NUMBER', 'TK_RIGHT_PAREN', 'TK_NUMBER', 'TK_EOL']
    def __parse_account_paren_number_number_line(self, line):
        return [
            line[0].get_value(),
            -self.string_utils.normalize_number(line[2].get_value()),
            self.string_utils.normalize_number(line[4].get_value())
        ]
        
    # ['TK_ACCOUNT', 'TK_NUMBER', 'TK_LEFT_PAREN', 'TK_NUMBER', 'TK_RIGHT_PAREN', 'TK_EOL']
    def __parse_account_number_paren_number_line(self, line):
        return [
            line[0].get_value(),
            self.string_utils.normalize_number(line[1].get_value()),
            -self.string_utils.normalize_number(line[3].get_value())
        ]

    # ['TK_ACCOUNT', 'TK_LEFT_PAREN', 'TK_NUMBER', 'TK_RIGHT_PAREN', 'TK_LEFT_PAREN', 'TK_NUMBER', 'TK_RIGHT_PAREN', 'TK_EOL']
    def __parse_account_paren_number_paren_number_line(self, line):
        return [
            line[0].get_value(),
            -self.string_utils.normalize_number(line[2].get_value()),
            -self.string_utils.normalize_number(line[5].get_value())
        ]
