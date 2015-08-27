#-*- coding: utf-8 -*-

from stockcat.state.taurus.state_machine import TaurusStateMachine
from stockcat.spider.dividend_policy_spider import DividendPolicySpider
from stockcat.assembler.dividend_policy_assembler import DividendPolicyAssembler
from stockcat.feed.dividend_policy_feed import DividendPolicyFeedBuilder

class StateMachine():
    def __init__(self, memento_path='dividend_policy_memento.json'):
        self.impl = TaurusStateMachine(
            memento_path,
            DividendPolicySpider(),
            DividendPolicyAssembler(),
            DividendPolicyFeedBuilder()
        )
        
    def run(self):
        self.impl.run()
