#-*- coding: utf-8 -*-

from stockcat.common.date_utils import DateUtils
from stockcat.common.string_utils import StringUtils

import lxml.html

class CancerParser():
    def __init__(self):
        self.base_xpath = '//html/body/center'
        self.date_utils = DateUtils()
        self.string_utils = StringUtils()

    def parse(self, content):
        html_object = self.__get_html_object(content) 
        relative_html_object = self.__traverse_to_relative_html_object(html_object)
        column_name_list = self.__parse_column_name_list(relative_html_object)
        row_list = self.__parse_row_list(relative_html_object)
        release_date = self.__parse_release_date(relative_html_object)
        return column_name_list, row_list, release_date

    def __get_html_object(self, content):
        content = self.string_utils.normalize_string(content)
        content = content.replace(u'<br>', u'')
        return lxml.html.fromstring(content)

    def __traverse_to_relative_html_object(self, html_object):
        relative_html_object_list = html_object.xpath(self.base_xpath)
        assert len(relative_html_object_list) > 0, 'invalid base_xpath'
        return relative_html_object_list[0]

    def __parse_column_name_list(self, relative_html_object):
        # traverse and sanity check
        table_tags = relative_html_object.xpath('./table')
        assert len(table_tags) > 1, 'invalid table_tags'

        # skip first table of description about IFRS
        inner_table_tags = table_tags[1].xpath('./tr/td/table/tr/td/table')
        assert len(inner_table_tags) > 0, 'invalid inner_table_tags'

        tr_tags = inner_table_tags[0].xpath('./tr')
        assert len(tr_tags) > 1, 'invalid tr_tags'

        th_texts = tr_tags[1].xpath('./th/text()')
        return th_texts

    def __parse_row_list(self, relative_html_object):
        # traverse and sanity check
        table_tags = relative_html_object.xpath('./table')
        assert len(table_tags) > 1, 'invalid table_tags'

        # skip first table of description about IFRS
        inner_table_tags = table_tags[1].xpath('./tr/td/table/tr/td/table')
        assert len(inner_table_tags) > 0, 'invalid inner_table_tags'

        all_tr_tags = []
        # every inner_table represents an industry
        for inner_table_tag in inner_table_tags:
            tr_tags = inner_table_tag.xpath('./tr')
            assert len(tr_tags) > 2, 'invalid tr_tags'
            # first two rows are headers
            # last row is u'合計'
            all_tr_tags += tr_tags[2:-1]
        return [self.__parse_row(tr_tag) for tr_tag in all_tr_tags]

    def __parse_row(self, relative_html_object):
        td_texts = relative_html_object.xpath('./td/text()')
        # summary contains extra entry about comment
        assert len(td_texts) == 11, 'invalid td_texts size, should be 11'

        items = td_texts[:2]

        numbers = []
        # skip the last entry about comment
        for td_text in td_texts[2:-1]:
            number = self.string_utils.normalize_number(td_text)
            numbers.append(number)

        return items + numbers    

    def __parse_release_date(self, relative_html_object):
        div_tags = relative_html_object.xpath('./div')
        assert len(div_tags) > 0, 'invalid div_tags'

        print div_tags[-1].text
        print type(div_tags[-1].text)

        groups = self.string_utils.match(u'^出表日期：(.*)$', div_tags[-1].text.strip())
        assert len(groups) > 0, 'could not match ^出表日期：(.*)$'
        
        release_date = self.string_utils.from_local_string_to_date(groups[0])
        return release_date