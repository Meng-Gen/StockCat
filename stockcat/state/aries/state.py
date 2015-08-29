#-*- coding: utf-8 -*-

import random
import time

class State():
    def run(self):
        pass

    def next(self):
        pass

    def avoid_blocking(self, a=3, b=5):
        time.sleep(random.randint(a, b))
