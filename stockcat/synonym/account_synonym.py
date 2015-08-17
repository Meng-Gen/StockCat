#-*- coding: utf-8 -*-

class AccountSynonym():
    def __init__(self):
        self.inverse_synonym = {
            u'當月營收' : [ u'本月', u'當月營收', ],
            u'現金增資' : [ u'現金增資', ], 
            u'盈餘轉增資' : [ u'盈餘轉增資', ],
            u'公積及其他' : [ u'公積及其他', ], 
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
