#-*- coding: utf-8 -*-

from string_utils import StringUtils

import lxml.html

class BalanceSheetAssembler():
    def __init__(self):
        self.base_xpath = '//html/body[@id="content_d"]/center/table[@class="result_table hasBorder"]'
        self.string_utils = StringUtils()

    def assemble(self, html_object):
        relative_html_object = self.__traverse_to_relative_html_object(html_object)
        column_name_list = self.__assemble_column_name_list(relative_html_object)
        row_list = self.__assemble_row_list(relative_html_object)
        return (column_name_list, row_list)

    def __traverse_to_relative_html_object(self, html_object):
        relative_html_object_list = html_object.xpath(self.base_xpath)
        assert len(relative_html_object_list) == 1, 'invalid base_xpath'
        return relative_html_object_list[0]

    def __assemble_column_name_list(self, relative_html_object):
        # traverse and sanity check
        tr_tags = relative_html_object.xpath('./tr[@class="tblHead"]')
        assert len(tr_tags) == 2, 'invalid tr_tags'

        # traverse and sanity check        
        statement_th_texts = tr_tags[1].xpath('./th/text()')
        assert len(statement_th_texts) == 1, 'invalid statement_th_texts'
        assert unicode(statement_th_texts[0]) == u'資產負債表', 'invalid statement_th_texts[0]'

        column_name_list = []
        
        # should be account type
        column_th_texts = tr_tags[0].xpath('./th/text()')
        account_type = column_th_texts[0] # of unicode type
        column_name_list.append(account_type)

        # should be snapshot dates
        for local_string in column_th_texts[1:]:
            snapshot_date = self.string_utils.from_local_string_to_date(local_string) # of datetime.date type
            column_name_list.append(snapshot_date)

        return column_name_list

    def __assemble_row_list(self, relative_html_object):
        odd_tr_tags = relative_html_object.xpath('./tr[@class="odd"]')
        even_tr_tags = relative_html_object.xpath('./tr[@class="even"]')
        tr_tags = self.__merge_parity_list(odd_tr_tags, even_tr_tags)
        return [self.__assemble_row(tr_tag) for tr_tag in tr_tags]

    def __assemble_row(self, relative_html_object):
        row = []

        td_texts = relative_html_object.xpath('./td/text()')

        # should be account type and its leading space count (determine the grade of account type)
        account_type = td_texts[0].strip()
        leading_space_count = len(td_texts[0]) - len(td_texts[0].lstrip())
        row.append((account_type, leading_space_count))

        # should be number
        for number_string in td_texts[1:]:
            number = self.string_utils.normalize_number(number_string)
            row.append(number)

        return row

    def __merge_parity_list(self, odd_list, even_list):
        odd_count = len(odd_list)
        even_count = len(even_list)
        assert odd_count == even_count or odd_count == even_count + 1
        
        final_list = []
        for i in range(even_count):
            final_list.append(odd_list[i])
            final_list.append(even_list[i])
        for i in range(even_count, odd_count):
            final_list.append(odd_list[i])
        return final_list