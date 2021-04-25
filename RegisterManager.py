from registermodel import Register
from random import uniform
from random import randint
import math
import json

class RegisterManager():
    def __init__(self):
        self._registers = []
    
    @property
    def money(self):
        if len(self._registers) == 0:
            return "There are no registers tied to the manager"
        else:
            money = 0
            for reg in self._registers:
                money = money + reg.get_total_made
            return "${:.2f}".format(money)
    
    def add_register(self,register):
        if not (register, Register):
            print("This is not a Register obj")
        else:
            add = True
            for reg in self._registers:
                if reg.id == register.id:
                    print("There is already a register under this ID")
                    add = False
                    break
            if add:
                self._registers.append(register)
    
    def remove_register(self,register):
        if not (register, Register):
            print("This is not a Register obj")
        else:
            drem = True
            for reg in self._registers:
                if reg.id == register.id:
                    self._registers.remove(register)
                    drem = False
                    break
            if drem:
                print("There is no register under this ID")
    
    def print_registers(self):
        if len(self._registers) == 0:
            print("There are no registers tied to the manager")
        else:
            registerids = []
            for reg in self._registers:
                registerids.append(reg.id)
            print("Registers: ",end='')
            print(', '.join(map(str,registerids)))
    
    def register_rundown(self,id):
        if len(self._registers) == 0:
            print("There are no registers tied to the manager")
        else:
            drd = True
            for reg in self._registers:
                if reg.id == id:
                    print("REGISTER {}:".format(id))
                    reg.rundown()
                    drd = False
                    break
            if drd:
                print("There is no register under this ID")
    
    def rundown(self):
        if len(self._registers) == 0:
            return "There are no registers tied to the manager"
        else:
            gettotalmade = 0
            cashmoneymade = 0
            debitmoneymade = 0
            creditmoneymade = 0
            giftcardmoneymade = 0
            moneyreturned = 0
            totaltrans = 0
            cashtrans = 0
            debittrans = 0
            credittrans = 0
            giftcardtrans = 0
            returntrans = 0
            itemspertrans = 0
            totalpurchasetrans = 0
            moneymade = 0
            for reg in self._registers:
                gettotalmade += reg.get_total_made
                cashmoneymade += reg._cash_money_made
                debitmoneymade += reg._debit_money_made
                creditmoneymade += reg._credit_money_made
                giftcardmoneymade += reg._giftcard_money_made
                moneyreturned += reg._money_returned
                totaltrans += reg.get_total_trans
                cashtrans += reg._cash_trans
                debittrans += reg._debit_trans
                credittrans += reg._credit_trans
                giftcardtrans += reg._giftcard_trans
                returntrans += reg._return_trans
                itemspertrans += reg._items_pertrans
                totalpurchasetrans += reg.get_total_purchase_trans
                moneymade += reg._money_made


            print('Total registers: {}'.format(len(self._registers)))
            print('Total money made: ${:.2f}'.format(gettotalmade))
            print('Money made by cash: ${:.2f}\nMoney made by debit: ${:.2f}\nMoney made by credit: ${:.2f}\nMoney made by giftcards: ${:.2f}'.format(cashmoneymade,debitmoneymade,creditmoneymade,giftcardmoneymade))
            print('Money returned: ${:.2f}'.format(moneyreturned))
            print('\nTotal transactions: {}\nNumber of cash transactions: {}\nNumber of debit transactions: {}\nNumber of credit transactions:{}\nNumber of giftcards transactions: {}\nNumber of return transactions: {}'.format(totaltrans,cashtrans,debittrans,credittrans,giftcardtrans,returntrans))
            print('\nCash in registers:')
            for reg in self._registers:
                print('Register {} - ${:.2f}'.format(reg.id,reg._cashinregister))
            print('\nItems purchased: {}\nAverage number of items per transaction: {:.2f}\nAverage cost per item: ${:.2f}\nAverage transaction cost: ${:.2f}'.format(itemspertrans,itemspertrans/totalpurchasetrans,moneymade/itemspertrans,moneymade/totalpurchasetrans))
  
    def rundown_json(self):
        if len(self._registers) == 0:
            print("There are no registers tied to the manager")
        else:
            gettotalmade = 0
            cashmoneymade = 0
            debitmoneymade = 0
            creditmoneymade = 0
            giftcardmoneymade = 0
            moneyreturned = 0
            totaltrans = 0
            cashtrans = 0
            debittrans = 0
            credittrans = 0
            giftcardtrans = 0
            returntrans = 0
            itemspertrans = 0
            totalpurchasetrans = 0
            moneymade = 0
            for reg in self._registers:
                gettotalmade += reg.get_total_made
                cashmoneymade += reg._cash_money_made
                debitmoneymade += reg._debit_money_made
                creditmoneymade += reg._credit_money_made
                giftcardmoneymade += reg._giftcard_money_made
                moneyreturned += reg._money_returned
                totaltrans += reg.get_total_trans
                cashtrans += reg._cash_trans
                debittrans += reg._debit_trans
                credittrans += reg._credit_trans
                giftcardtrans += reg._giftcard_trans
                returntrans += reg._return_trans
                itemspertrans += reg._items_pertrans
                totalpurchasetrans += reg.get_total_purchase_trans
                moneymade += reg._money_made
            all_regs = {
                'money_details':{
                    'total_money_made':round(gettotalmade,2),
                    'cash':round(cashmoneymade,2),
                    'debit':round(debitmoneymade,2),
                    'credit':round(creditmoneymade,2),
                    'giftcard':round(giftcardmoneymade,2),
                    'returned':round(moneyreturned,2)
                },
                'transaction_details':{
                    'total_transactions':totaltrans,
                    'cash':cashtrans,
                    'debit':debittrans,
                    'credit':credittrans,
                    'giftcard':giftcardtrans,
                    'return':returntrans,
                },
                'cash_in_registers':{},
                'stats':{
                    'items_purchased':itemspertrans,
                    'avg_item_per_trans':round(itemspertrans/totalpurchasetrans,2),
                    'avg_cost_per_item':round(moneymade/itemspertrans,2),
                    'avg_trans_cost':round(moneymade/totalpurchasetrans,2)
                }
            }
            for reg in self._registers:
                all_regs['cash_in_registers']['Register {}'.format(reg.id)] = round(reg._cashinregister,2)
            json_export = {}
            json_export['all_registers'] = all_regs
            for reg in self._registers:
                json_export['register_{}'.format(reg.id)] = reg.rundown_dict()
            with open('registers_rundown.json','w') as file:
                json.dump(json_export, file)

def fill(regi):
    def grp():
        return round(uniform(40,100),2)
    def gri():
        return round(uniform(1,10))
    def grt():
        return round(uniform(50,200))

    def group_cash(reg):
        for i in range(grt()):
            price = grp()
            reg.cash_transaction(price,math.ceil(price),gri())
    def group_debit(reg):
        for i in range(grt()):
            reg.debit_transaction(grp(),gri())
    def group_credit(reg):
        for i in range(grt()):
            reg.credit_transaction(grp(),gri())
    def group_giftcard(reg):
        for i in range(grt()):
            reg.giftcard_transaction(grp(),gri())
    def group_return(reg):
        methods = ['cash','credit','debit','giftcard']
        for i in range(grt()):
            method_i = randint(0,3)
            reg.return_item(methods[method_i],grp()/2)
    group_cash(regi)
    group_credit(regi)
    group_debit(regi)
    group_giftcard(regi)
    group_return(regi)

if __name__=="__main__":
    rm = RegisterManager()
    reg1 = Register(1,250)
    reg2 = Register(2,250)
    reg3 = Register(3,250)

    fill(reg1)
    fill(reg2)
    fill(reg3)

    rm.add_register(reg1)
    rm.add_register(reg2)
    rm.add_register(reg3)
    rm.rundown_json()