#-*- coding: utf-8 -*-

from stockcat.common.logging_utils import setup_logging
from stockcat.initializer import Initializer

import logging
import sys 

def main():
    setup_logging() 
    initializer = Initializer()
    #initializer.init_stock_symbol()
    initializer.init_operating_revenue_summary()

if __name__ == '__main__':
    sys.exit(main())