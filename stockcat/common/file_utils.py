#-*- coding: utf-8 -*-

import urllib2

class FileUtils():
    def copy_url_to_file(self, url_spec, filepath):
        response = urllib2.urlopen(url_spec)
        content = response.read()
        with open(filepath, 'w+') as file_handle:
            file_handle.write(content)

    def read_file(self, filepath):
        content = None
        with open(filepath) as file_handle:
            content = file_handle.read().replace('\n', '')
        return content