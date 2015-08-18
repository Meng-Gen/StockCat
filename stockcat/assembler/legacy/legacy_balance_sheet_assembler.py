#-*- coding: utf-8 -*-

from stockcat.common.string_utils import StringUtils
from stockcat.dao.balance_sheet_dao import BalanceSheetDao

import lxml.html

class LegacyBalanceSheetAssembler():
    def __init__(self):
        self.base_xpath = '//html/body/table/table'
        self.string_utils = StringUtils()

    def assemble(self, content, stock_symbol, date):
        content = self.string_utils.normalize_string(content)
        html_object = lxml.html.fromstring(content)
        relative_html_object = self.__traverse_to_relative_html_object(html_object)
        column_name_list = self.__assemble_column_name_list(relative_html_object)
        row_list = self.__assemble_row_list(relative_html_object)
        return BalanceSheetDao(column_name_list, row_list, stock_symbol, date)

    def __traverse_to_relative_html_object(self, html_object):
        relative_html_object_list = html_object.xpath(self.base_xpath)
        assert len(relative_html_object_list) == 1, 'invalid base_xpath'
        return relative_html_object_list[0]

    def __assemble_column_name_list(self, relative_html_object):
        # traverse and sanity check
        tr_tags = relative_html_object.xpath('./tbody/tr')
        assert len(tr_tags) == 5, 'invalid tr_tags'

        column_name_list = []

        # should be account type
        column_th_texts = tr_tags[3].xpath('./th/b/text()')
        account_type = column_th_texts[0] # of unicode type
        column_name_list.append(account_type)

        for local_string in column_th_texts[1:]:
            # of datetime.date type
            snapshot_date = self.string_utils.from_local_string_to_date(local_string) 
            column_name_list.append(snapshot_date)

        return column_name_list

    def __assemble_row_list(self, relative_html_object):
        tr_tags = relative_html_object.xpath('./tr')
        return [self.__assemble_row(tr_tag) for tr_tag in tr_tags]

    def __assemble_row(self, relative_html_object):
        row = []

        td_texts = relative_html_object.xpath('./td/text()')
        td_texts = self.__remove_empty_string_from_string_list(td_texts)

        # should be account type and its leading space count (determine the grade of account type)
        account_type = td_texts[0].strip()
        leading_space_count = len(td_texts[0]) - len(td_texts[0].lstrip())
        row.append((account_type, leading_space_count))

        # should be number (skip percentage number)
        for i in range(1, len(td_texts), 2):
            number_string = td_texts[i]
            number = self.string_utils.normalize_number(number_string)
            row.append(number)

        return row

    def __remove_empty_string_from_string_list(self, string_list):
        return [string for string in string_list if string.strip()]
