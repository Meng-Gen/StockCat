#-*- coding: utf-8 -*-

import os
import os.path

class FileUtils():
    def join_paths(self, path, *paths):
        return os.path.join(path, *paths)

    def copy_url_to_file(self, url, filepath):
        # if directory is not existed, need to create by ourselves
        self.__make_directory(filepath)

        # use build-in curl program to retrieve content from web servers
        self.__curl(url, filepath)

    def read_file(self, filepath):
        content = None
        with open(filepath) as file_handle:
            content = file_handle.read().replace('\n', '')
        return content

    def is_file(self, filepath):
        return os.path.isfile(filepath) 

    def __make_directory(self, filepath):
        directory = os.path.dirname(os.path.realpath(filepath))
        if not os.path.exists(directory):
            os.makedirs(directory)

    def __curl(self, url, filepath):
        params = '''-o \"{filepath}\" \"{url}\" --connect-timeout 5 --max-time 10 --retry 5 --retry-delay 0 --retry-max-time 60'''.format(url=url, filepath=filepath)
        cmdline = '''curl {params}'''.format(params=params)
        os.system(cmdline)
        