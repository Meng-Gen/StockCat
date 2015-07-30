#-*- coding: utf-8 -*-

import os.path
import urllib2

class FileUtils():
    def copy_url_to_file(self, url_spec, filepath):
        self.__make_directory(filepath)
        response = urllib2.urlopen(url_spec)
        content = response.read()
        with open(filepath, 'w+') as file_handle:
            file_handle.write(content)

    def read_file(self, filepath):
        content = None
        with open(filepath) as file_handle:
            content = file_handle.read().replace('\n', '')
        return content

    def __make_directory(self, filepath):
        directory = os.path.dirname(os.path.realpath(filepath))
        if not os.path.exists(directory):
            os.makedirs(directory)
