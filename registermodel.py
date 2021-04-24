from random import uniform
from random import randint
import math
import json

class Register():
    def __init__(self,id,startingcash):
        if isinstance(id, bool):
            raise TypeError
        if not isinstance(id, int):
            raise TypeError
        if isinstance(float(startingcash), bool):
            raise TypeError
        if not isinstance(float(startingcash), float):
            raise TypeError
    
        self._id = id

        self._startingcash = float(startingcash)
        self._cashinregister = float(startingcash)

        self._money_made = 0.0
        self._money_returned = 0.0
        self._return_trans = 0

        self._items_pertrans = 0

        self._cash_trans = 0
        self._cash_money_made = 0.0

        self._debit_trans = 0
        self._debit_money_made = 0.0

        self._credit_trans = 0
        self._credit_money_made = 0.0

        self._giftcard_trans = 0
        self._giftcard_money_made = 0.0
    
    @property
    def get_total_made(self):
        return self._money_made-self._money_returned
    @property
    def get_total_trans(self):
        return self._return_trans+self._debit_trans+self._cash_trans+self._credit_trans+self._giftcard_trans
    @property
    def get_total_purchase_trans(self):
        return self._debit_trans+self._cash_trans+self._credit_trans+self._giftcard_trans
    @property
    def id(self):
        return self._id

    def cash_transaction(self,price,cashgiven,items):
        self._money_made = self._money_made + price
        self._cashinregister = self._cashinregister + price
        self._cash_money_made = self._cash_money_made + price
        self._cash_trans += 1
        self._items_pertrans = self._items_pertrans + items
        #print("Change for customer: {:.2f}".format(cashgiven-price))
    
    def debit_transaction(self,price,items):
        self._money_made = self._money_made + price
        self._debit_money_made = self._debit_money_made + price
        self._debit_trans += 1
        self._items_pertrans = self._items_pertrans + items
    
    def credit_transaction(self,price,items):
        self._money_made = self._money_made + price
        self._credit_money_made = self._credit_money_made + price
        self._credit_trans += 1
        self._items_pertrans = self._items_pertrans + items
    
    def giftcard_transaction(self,price,items):
        self._money_made = self._money_made + price
        self._giftcard_money_made = self._giftcard_money_made + price
        self._giftcard_trans += 1
        self._items_pertrans = self._items_pertrans + items

    def return_item(self,method,rvalue):
        cont = True
        if method == 'cash':
            if rvalue > self._cashinregister:
                cont = False
            else:
                self._cashinregister = self._cashinregister - rvalue
        if cont:
            self._money_returned = self._money_returned + rvalue
            self._return_trans += 1
        else:
            print('Not enough money in the register!')

    
    def rundown(self):
        print('Total money made: ${:.2f}'.format(self.get_total_made))
        print('Money made by cash: ${:.2f}\nMoney made by debit: ${:.2f}\nMoney made by credit: ${:.2f}\nMoney made by giftcards: ${:.2f}'.format(self._cash_money_made,self._debit_money_made,self._credit_money_made,self._giftcard_money_made))
        print('Money returned: ${:.2f}'.format(self._money_returned))
        print('\nTotal transactions: {}\nNumber of cash transactions:{}\nNumber of debit transactions:{}\nNumber of credit transactions:{}\nNumber of giftcards transactions:{}\nNumber of return transactions:{}'.format(self.get_total_trans,self._cash_trans,self._debit_trans,self._credit_trans,self._giftcard_trans,self._return_trans))
        print('\nCash in register: ${:.2f}'.format(self._cashinregister))
        print('\nItems purchased: {}\nAverage number of items per transaction: {:.2f}\nAverage cost per item: ${:.2f}\nAverage transaction cost: ${:.2f}'.format(self._items_pertrans,self._items_pertrans/self.get_total_purchase_trans,self._money_made/self._items_pertrans,self._money_made/self.get_total_purchase_trans))
    
    def rundown_json(self):
        json_export = {
            'money_details':{
                'total_money_made':round(self.get_total_made,2),
                'cash':round(self._cash_money_made,2),
                'debit':round(self._debit_money_made,2),
                'credit':round(self._credit_money_made,2),
                'giftcard':round(self._giftcard_money_made,2),
                'returned':round(self._money_returned,2)
            },
            'transaction_details':{
                'total_transactions':self.get_total_trans,
                'cash':self._cash_trans,
                'debit':self._debit_trans,
                'credit':self._credit_trans,
                'giftcard':self._giftcard_trans,
                'return':self._return_trans,
            },
            'cash_in_register':round(self._cashinregister,2),
            'stats':{
                'items_purchased':self._items_pertrans,
                'avg_item_per_trans':round(self._items_pertrans/self.get_total_purchase_trans,2),
                'avg_cost_per_item':round(self._money_made/self._items_pertrans,2),
                'avg_trans_cost':round(self._money_made/self.get_total_purchase_trans,2)
            }
        }
        with open('register_'+str(self._id)+'_rundow.json', 'w') as file:
            json.dump(json_export, file)