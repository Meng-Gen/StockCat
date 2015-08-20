#-*- coding: utf-8 -*-

from stockcat.assembler.legacy.cash_flow_parser.scanner import Scanner
from stockcat.assembler.legacy.cash_flow_parser.source import Source
from stockcat.common.account_utils import AccountUtils
from stockcat.common.string_utils import StringUtils

import lxml.html

class AriesParser():
    def __init__(self, text):
        self.text = text
        self.head_splitted_account = None
        self.account_utils = AccountUtils()
        self.string_utils = StringUtils()

    def parse(self):
        text = self.account_utils.concat_account(self.text)
        lines = self.__scan_lines(text)
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

        assert visited_column_name_list, 'We should parse column name list'
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
