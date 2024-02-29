import bank_data as bd
class InvalidDigit(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
class InsufficientBalance(Exception):
    def __init__(self,msg='Insufficient Balance.'):
        self.msg=msg
    def __str__(self):
        return self.msg
class customer:
    def __init__(self,bank_data):
        self.bank_data=bank_data#testing purpose

    def withdraw_amount(self,acc_number,withdraw):
        try: 
            #if not (str(acc_number).isdigit() or str(withdraw).isdigit()):  
            if str(acc_number).isdigit()==False or str(withdraw).isdigit()==False:
                raise InvalidDigit('Account number and Withdrawn amount should be in digits only.')
            if acc_number not in self.bank_data.get_data_acc().keys():
                return print('Account does not exists.')         
            if not (0<=withdraw<=self.bank_data.get_data_acc()[acc_number]['Balance']):
                raise InsufficientBalance
            self.bank_data.get_data_acc()[acc_number]['Balance']-=withdraw
            print(f'Withdrawal Amount:{withdraw} Updated balance:{self.bank_data.get_data_acc()[acc_number]["Balance"]}')  

            self.bank_data.save_data()
        except (InvalidDigit,InsufficientBalance) as err:
            print(err)
        

    def deposit_amount(self,acc_number,deposit):
        try:
            if not (str(acc_number).isdigit()) or  not (str(deposit).isdigit()):
                raise InvalidDigit('Account number and deposit should be in digits only.')
            if acc_number not in self.bank_data.get_data_acc().keys():
                return print(f'No such account exist.')
            if deposit>=0:
                    self.bank_data.get_data_acc()[acc_number]['Balance']+=deposit
                    print(f'Deposited Amount {deposit}.Updated Balance:{self.bank_data.get_data_acc()[acc_number]["Balance"]}')
            
            self.bank_data.save_data()
            if deposit<0:
                raise InvalidDigit('Enter positive digit.')
        except InvalidDigit as err:
            print(err)
    
    def view_balance(self,acc_number):
        try:
            if str(acc_number).isdigit()==False:
                raise InvalidDigit('Account number must be digits only.')
            if acc_number not in self.bank_data.get_data_acc().keys():
                return print(f'No such data exist')
            print(f"Your account {acc_number} balance is:{self.bank_data.get_data_acc()[acc_number]['Balance']}")  
        except InvalidDigit as err:
            print(err)
if __name__=='__main__':#testing purpose
    akshay_customer=customer(bd.BankData())
    akshay_customer.deposit_amount(103,5000)
    akshay_customer.view_balance(103)
    akshay_customer.withdraw_amount(103,5000)