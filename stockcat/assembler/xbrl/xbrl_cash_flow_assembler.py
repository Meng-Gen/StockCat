#-*- coding: utf-8 -*-

from stockcat.common.string_utils import StringUtils
from stockcat.dao.cash_flow_dao import CashFlowDao

import lxml.html

class XbrlCashFlowAssembler():
    def __init__(self):
        self.base_xpath = '//html/body[@id="content_d"]/center/table[@class="main_table hasBorder"]'
        self.string_utils = StringUtils()

    def assemble(self, param):
        content, stock_symbol, date = param['content'], param['stock_symbol'], param['date']
        content = self.string_utils.normalize_string(content)
        html_object = lxml.html.fromstring(content)
        relative_html_object = self.__traverse_to_relative_html_object(html_object)
        column_name_list = self.__assemble_column_name_list(relative_html_object)
        row_list = self.__assemble_row_list(relative_html_object)
        return CashFlowDao(column_name_list, row_list, stock_symbol, date)

    def __traverse_to_relative_html_object(self, html_object):
        relative_html_object_list = html_object.xpath(self.base_xpath)
        assert len(relative_html_object_list) > 1, 'invalid base_xpath'
        return relative_html_object_list[1]

    def __assemble_column_name_list(self, relative_html_object):
        # traverse and sanity check
        tr_tags = relative_html_object.xpath('./tr[@class="tblHead"]')
        assert len(tr_tags) == 2, 'invalid tr_tags'

        # traverse and sanity check        
        statement_th_texts = tr_tags[1].xpath('./th/text()')
        assert len(statement_th_texts) == 1, 'invalid statement_th_texts'
        assert unicode(statement_th_texts[0]) == u'現金流量表', 'invalid statement_th_texts[0]'

        column_name_list = []
        
        # should be account type
        column_th_texts = tr_tags[0].xpath('./th/text()')
        account_type = column_th_texts[0] # of unicode type
        column_name_list.append(account_type)

        # should be date interval
        for local_string in column_th_texts[1:]:
            # of (datetime.date, datetime.date) type
            snapshot_date = self.string_utils.from_local_string_to_date_period(local_string) 
            column_name_list.append(snapshot_date)

        return column_name_list

    def __assemble_row_list(self, relative_html_object):
        # skip one row of statement name and one row of column name list
        tr_tags = relative_html_object.xpath('./tr')[2:]
        return [self.__assemble_row(tr_tag) for tr_tag in tr_tags]

    def __assemble_row(self, relative_html_object):
        row = []

        td_texts = relative_html_object.xpath('./td/text()')

        # should be account type 
        account_type = td_texts[0].strip()
        row.append(account_type)

        # should be number
        for number_string in td_texts[1:]:
            number = self.string_utils.normalize_number(number_string)
            row.append(number)

        return row
