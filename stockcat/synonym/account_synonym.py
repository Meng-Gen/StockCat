#-*- coding: utf-8 -*-

class AccountSynonym():
    def __init__(self):
        self.inverse_synonym = {
            u'本月' : [ u'本月' ],
            u'去年同期' : [ u'去年同期' ], 
        }
        self.synonym = self.__init_synonym()

    def __init_synonym(self):
        result = {}
        for unique_term in self.inverse_synonym:
            for synonym_term in self.inverse_synonym[unique_term]:
                result[synonym_term] = unique_term
        return result

    def get(self, term):
        if term in self.synonym: 
            return self.synonym[term]
        else:
            return term
