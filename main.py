#-*- coding: utf-8 -*-

from stockcat.common.logging_utils import setup_logging
from stockcat.stock_cat import StockCat
import sys 

def main():
    setup_logging() 
    stock_cat = StockCat()
    stock_cat.run()
    #cat.debug_default_memento()
    
if __name__ == '__main__':
    sys.exit(main())