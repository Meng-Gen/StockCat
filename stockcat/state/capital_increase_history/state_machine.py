#-*- coding: utf-8 -*-

from stockcat.state.taurus.state_machine import TaurusStateMachine
from stockcat.spider.capital_increase_history_spider import CapitalIncreaseHistorySpider
from stockcat.assembler.capital_increase_history_assembler import CapitalIncreaseHistoryAssembler
from stockcat.feed.capital_increase_history_feed import CapitalIncreaseHistoryFeedBuilder

class StateMachine():
    def __init__(self, memento_path='capital_increase_history_memento.json'):
        self.impl = TaurusStateMachine(
            memento_path,
            CapitalIncreaseHistorySpider(),
            CapitalIncreaseHistoryAssembler(),
            CapitalIncreaseHistoryFeedBuilder()
        )
        
    def run(self):
        self.impl.run()
