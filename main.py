#-*- coding: utf-8 -*-

import datetime
import sys

def analyze_capital_increase_history():
    from stockcat.analyzer.capital_increase_history_analyzer import CapitalIncreaseHistoryAnalyzer
    analyzer = CapitalIncreaseHistoryAnalyzer()
    stock_symbol_list = analyzer.get_stock_symbol_list()
    print stock_symbol_list[:10]    

def main():
    analyze_capital_increase_history()

if __name__ == '__main__':
    sys.exit(main())