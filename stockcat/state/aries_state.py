#-*- coding: utf-8 -*-

import random
import time

class AriesState():
    def run(self):
        raise NotImplementedError, 'we should implement the abstract method' 

    def next(self):
        raise NotImplementedError, 'we should implement the abstract method' 
        
    def avoid_blocking(self, a=3, b=5):
        time.sleep(random.randint(a, b))
