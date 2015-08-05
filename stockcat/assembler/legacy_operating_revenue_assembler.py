#-*- coding: utf-8 -*-

from stockcat.common.string_utils import StringUtils

import lxml.html

class LegacyOperatingRevenueAssembler():
    def __init__(self):
        self.base_xpath = '//html/body/table[@class="hasBorder"]'
        self.string_utils = StringUtils()

    def assemble(self, content):
        html_object = lxml.html.fromstring(content)
        relative_html_object = self.__traverse_to_relative_html_object(html_object)
        column_name_list = self.__assemble_column_name_list(relative_html_object)
        row_list = self.__assemble_row_list(relative_html_object)
        return (column_name_list, row_list)

    def __traverse_to_relative_html_object(self, html_object):
        relative_html_object_list = html_object.xpath(self.base_xpath)
        assert len(relative_html_object_list) > 1, 'invalid base_xpath'
        # skip the first table because it is irrelevant
        return relative_html_object_list[1]

    def __assemble_column_name_list(self, relative_html_object):
        # traverse and sanity check
        tr_tags = relative_html_object.xpath('./tr')
        assert len(tr_tags) > 0, 'invalid tr_tags'

        # traverse and sanity check
        column_name_list = tr_tags[0].xpath('./td[@class="tblHead"]/text()')
        assert len(column_name_list) == 2, 'invalid column_name_list size, should be 2'
        return column_name_list

    def __assemble_row_list(self, relative_html_object):
        # skip the first row of column name list
        # skip the last row of comments
        tr_tags = relative_html_object.xpath('./tr')[1:-1]
        return [self.__assemble_row(tr_tag) for tr_tag in tr_tags]

    def __assemble_row(self, relative_html_object):
        # should be item
        th_texts = relative_html_object.xpath('./th/text()')
        assert len(th_texts) == 1, 'invalid th_texts size, should be 1'
        item = th_texts[0]

        # should be number (operating revenue)
        td_texts = relative_html_object.xpath('./td/text()')
        assert len(th_texts) == 1, 'invalid td_texts size, should be 1'
        number_string = td_texts[0]
        number = self.string_utils.normalize_number(number_string)

        return [item, number]
