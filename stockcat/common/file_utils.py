#-*- coding: utf-8 -*-

from stockcat.common.user_agent import UserAgent

import os
import os.path

class FileUtils():
    def __init__(self):
        self.user_agent = UserAgent()

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
            content = file_handle.read()
        return content

    def is_file(self, filepath):
        return os.path.isfile(filepath) 

    def __make_directory(self, filepath):
        directory = os.path.dirname(os.path.realpath(filepath))
        if not os.path.exists(directory):
            os.makedirs(directory)

    def __curl(self, url, filepath):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
        cookie = 'jcsession=jHttpSession@cb3542; newmops2=selfObj%3DtagCon1%7C'
        params = '''-o \"{filepath}\" \"{url}\" --connect-timeout 5 --max-time 10 --retry 5 --retry-delay 0 --retry-max-time 60 -A \"{user_agent}\" --cookie \"{cookie}\"'''.format(url=url, filepath=filepath, user_agent=user_agent, cookie=cookie)
        cmdline = '''curl {params}'''.format(params=params)
        os.system(cmdline)
        