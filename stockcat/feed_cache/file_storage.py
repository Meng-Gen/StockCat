#-*- coding: utf-8 -*-

from stockcat.common.file_utils import FileUtils

class FileStorage():
    def __init__(self):
        self.base_path = "./stockcat/data/"
        self.relative_path = {
            "stock_symbol.stock_exchange_market" : "stock_symbol/stock_exchange_market.html",
            "stock_symbol.otc_market" : "stock_symbol/otc_market.html", 
        }

        self.file_utils = FileUtils()

    def set(self, feed_name, url):
        filepath = self.file_utils.join_paths(self.base_path, self.relative_path[feed_name])
        self.file_utils.copy_url_to_file(url, filepath)

    def get(self, feed_name):
        filepath = self.file_utils.join_paths(self.base_path, self.relative_path[feed_name])
        return self.file_utils.read_file(filepath)
