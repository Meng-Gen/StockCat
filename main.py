#-*- coding: utf-8 -*-

from stockcat.common.logging_utils import setup_logging
from stockcat.cat import Cat
import sys 

def main():
    setup_logging() 
    cat = Cat()
    cat.run()
    
if __name__ == '__main__':
    sys.exit(main())