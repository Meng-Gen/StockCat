#-*- coding: utf-8 -*-

class AccountUtils():
    def __init__(self):
        self.concat_account_map = {
            u'合 併 現 金 流 量 表' : u'合併現金流量表', 
            u'換出資產 抵減價款' : u'換出資產抵減價款',
            u'換出資產  抵減價款' : u'換出資產抵減價款', 
            u'換出資產　抵減價款' : u'換出資產抵減價款', # two fullwidth spaces
            u'支付 現金金額' : u'支付現金金額', 
            u'取得 現金金額' : u'取得現金金額',
            u'存　　貨' : u'存貨', # two fullwidth spaces
            u'項        目' : u'項目', 
            u'(調整後)' : u'調整後',
            u'減: 少數股權' : u'減：少數股權', 
            u'九 十 八 年 度' : u'98年度',
            u'九 十 七 年 度' : u'97年度',
            u'九 十 六年度' : u'96年度',
            u'九 十 五年度' : u'95年度',
        }
        self.eten_separation_list = [
            u'┌', u'┬', u'┐', u'├', u'┼', u'┤', u'└', u'┴', u'┘', u'│', u'─', 
        ]

    def concat_account(self, text):
        for key in self.concat_account_map:
            text = text.replace(key, self.concat_account_map[key])
        return text

    def remove_eten_separation(self, text):
        for eten_separation in self.eten_separation_list:
            text = text.replace(eten_separation, '')
        return text
