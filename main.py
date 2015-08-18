#-*- coding: utf-8 -*-

import datetime
import sys

def analyze_capital_increase_history():
    from stockcat.analyzer.capital_increase_history_analyzer import CapitalIncreaseHistoryAnalyzer
    analyzer = CapitalIncreaseHistoryAnalyzer()
    capital_increase_by_cash = analyzer.get_capital_increase_by_cash('2498')
    print capital_increase_by_cash[:10]    

def main():
    analyze_capital_increase_history()

if __name__ == '__main__':
    sys.exit(main())