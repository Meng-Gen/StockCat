#-*- coding: utf-8 -*-

class AccountUtils():
    def __init__(self):
        self.concat_account_map = {
            u'換出資產 抵減價款' : u'換出資產抵減價款',
            u'支付 現金金額' : u'支付現金金額', 
            u'取得 現金金額' : u'取得現金金額',
            # two fullwidth spaces
            u'存　　貨' : u'存貨', 
            u'合 併 現 金 流 量 表' : u'合併現金流量表', 
        }

    def concat_account(self, text):
        for key in self.concat_account_map:
            text = text.replace(key, self.concat_account_map[key])
        return text