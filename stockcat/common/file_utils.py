#-*- coding: utf-8 -*-

import os
import os.path

class FileUtils():
    def join_paths(self, path, *paths):
        return os.path.join(path, *paths)

    def copy_url_to_file(self, url, filepath):
        # if directory is not existed, need to create by ourselves
        self.__make_directory(filepath)

        # use build-in wget program to retrieve content from web servers
        params = '\"{url}\" --waitretry=3 -O \"{filepath}\"'.format(url=url, filepath=filepath)
        cmdline = 'wget {params}'.format(params=params)
        os.system(cmdline)

    def read_file(self, filepath):
        content = None
        with open(filepath) as file_handle:
            content = file_handle.read().replace('\n', '')
        return content

    def __make_directory(self, filepath):
        directory = os.path.dirname(os.path.realpath(filepath))
        if not os.path.exists(directory):
            os.makedirs(directory)
