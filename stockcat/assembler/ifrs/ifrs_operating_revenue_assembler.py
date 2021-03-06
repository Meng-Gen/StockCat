#-*- coding: utf-8 -*-

from stockcat.assembler.content_screener import ContentScreener
from stockcat.common.string_utils import StringUtils
from stockcat.dao.operating_revenue_dao import OperatingRevenueDao

import lxml.html

class IfrsOperatingRevenueAssembler():
    def __init__(self):
        self.base_xpath = '//html/body'
        self.content_screener = ContentScreener()
        self.string_utils = StringUtils()

    def assemble(self, param):
        content, stock_symbol, date = param['content'], param['stock_symbol'], param['date']
        self.content_screener.screen(param)
        content = self.string_utils.normalize_string(content)
        html_object = lxml.html.fromstring(content)
        relative_html_object = self.__traverse_to_relative_html_object(html_object)
        column_name_list = self.__assemble_column_name_list(relative_html_object)
        row_list = self.__assemble_row_list(relative_html_object)
        return OperatingRevenueDao(column_name_list, row_list, stock_symbol, date)

    def __traverse_to_relative_html_object(self, html_object):
        relative_html_object_list = html_object.xpath(self.base_xpath)
        assert len(relative_html_object_list) > 0, 'invalid base_xpath'
        return relative_html_object_list[0]

    def __assemble_column_name_list(self, relative_html_object):
        # traverse and sanity check
        tr_tags = relative_html_object.xpath('./table[@class="hasBorder"]/tr')
        assert len(tr_tags) > 0, 'invalid tr_tags'

        # traverse and sanity check
        th_texts = tr_tags[0].xpath('./th/text()')
        assert len(th_texts) == 2, 'invalid th_texts size, should be 2'
        # should be account
        account = th_texts[0]

        # traverse and sanity check
        table_tags = relative_html_object.xpath('./table[@class="noBorder"]')
        assert len(table_tags) > 0, 'invalid table_tags'
        td_tags = table_tags[2].xpath('./td')
        assert len(td_tags) > 0, 'invalid td_tags'
        # should be snapdate
        snapdate = self.string_utils.from_local_string_to_date(td_tags[1].text)

        return [account, snapdate]

    def __assemble_row_list(self, relative_html_object):
        # skip one row of column name list
        tr_tags = relative_html_object.xpath('./table[@class="hasBorder"]/tr')[1:]
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
