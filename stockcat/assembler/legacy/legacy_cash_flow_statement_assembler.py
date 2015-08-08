#-*- coding: utf-8 -*-

from stockcat.common.string_utils import StringUtils

import lxml.html

class DeloitteParser():
    def __init__(self, text):
        self.text = text
        self.head_splitted_account = None
        self.string_utils = StringUtils()

    def parse(self):
        column_name_list = self.__parse_column_name_list()
        row_list = self.__parse_row_list()
        return column_name_list, row_list

    def __parse_column_name_list(self):
        lines = self.text.splitlines()
        # sanity check 
        assert lines[2].strip() == u'合併現金流量表'

        column_name_list = [u'會計科目']
        for local_string in lines[7].split():
            date_interval = self.string_utils.from_local_string_to_date_interval(local_string)
            snapshot_date = date_interval[1]
            column_name_list.append(snapshot_date)
        return column_name_list

    def __parse_row_list(self):
        # 7th row is column name list
        lines = self.text.splitlines()[8:]
        return [self.__parse_row(local_string) for local_string in lines]

    def __parse_row(self, local_string):
        tokens = self.__scan_tokens(local_string)
        if not tokens:
            return []

        row = []

        # should be account (splitted or not) and its leading space count
        # we will combine two splitted accounts as one if splitted
        account_type = self.__parse_account(tokens[0])
        if not account_type:
            return []
        else:
            leading_space_count = len(local_string) - len(local_string.lstrip())
            row.append((account_type, leading_space_count))
        # should be number
        for number_string in tokens[1:]:
            number = self.string_utils.normalize_number(number_string)
            row.append(number)

        return row

    def __parse_account(self, account):
        if self.__is_tail_splitted_account(account):
            assert self.head_splitted_account
            return self.head_splitted_account + account
        elif self.__is_head_splitted_account(account):
            self.head_splitted_account = account
            return None
        else:
            self.head_splitted_account = None
            return account

    def __scan_tokens(self, local_string):
        if self.__is_seperation(local_string):
            return []
        else:
            return self.__scan_account(local_string)

    def __is_seperation(self, local_string):
        return self.string_utils.is_match(u'^(-| |=)*$', local_string)

    def __scan_account(self, local_string):
        m = self.string_utils.match(u'^([^\s]*)：$', local_string.strip())
        if m:
            return m
        else:
            return self.__scan_account_without_colon(local_string)

    def __scan_account_without_colon(self, local_string):
        m = self.string_utils.match(u'^([^\s]*)$', local_string.strip())
        if m:
            return m
        else:
            return self.__scan_account_dollar_number_dollar_number(local_string)

    def __scan_account_dollar_number_dollar_number(self, local_string):
        m = self.string_utils.match(u'^([^\s]*)\s*\$\s*([^\s]*)\s*\$\s*([^\s]*)$', local_string.strip())
        if m:
            return m
        else:
            return self.__scan_account_negative_number_negative_number(local_string)

    def __scan_account_negative_number_negative_number(self, local_string):
        m = self.string_utils.match(u'^([^\s]*)\s*(\(.*\))\s*(\(.*\))$', local_string.strip())
        if m:
            return m
        else:
            return self.__scan_account_positive_number_negative_number(local_string)

    def __scan_account_positive_number_negative_number(self, local_string):
        m = self.string_utils.match(u'^([^\s]*)\s*(.*)\s*(\(.*\))$', local_string.strip())
        if m:
            return m
        else:
            return self.__scan_account_negative_number_positive_number(local_string)

    def __scan_account_negative_number_positive_number(self, local_string):
        m = self.string_utils.match(u'^([^\s]*)\s*(\(.*\))\s*(.*)$', local_string.strip())
        if m:
            return m
        else:
            return self.__scan_account_positive_number_positive_number(local_string)

    def __scan_account_positive_number_positive_number(self, local_string):
        m = self.string_utils.match(u'^([^\s]*)\s*([^\s]*)\s*([^\s]*)$', local_string.strip())
        if m:
            return m
        else:
            raise NotImplementedError

    def __is_head_splitted_account(self, account):
        return u'（' in account and u'）' not in account

    def __is_tail_splitted_account(self, account):
        return u'（' not in account and u'）' in account

class LegacyCashFlowStatementAssembler():
    def __init__(self):
        self.base_xpath = '//html/body/table[@class="hasBorder"]/tr/td/pre'
        self.string_utils = StringUtils()

    def assemble(self, content):
        content = self.string_utils.normalize_string(content)
        html_object = lxml.html.fromstring(content)
        relative_html_object = self.__traverse_to_relative_html_object(html_object)

        # Parse deloitte cash flow statement 
        parser = DeloitteParser(relative_html_object.text)
        column_name_list, row_list = parser.parse()
        return (column_name_list, row_list)

    def __traverse_to_relative_html_object(self, html_object):
        relative_html_object_list = html_object.xpath(self.base_xpath)
        assert len(relative_html_object_list) == 1, 'invalid base_xpath'
        return relative_html_object_list[0]
