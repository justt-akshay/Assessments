import json
import bank_data as bd
class NegativeAccountNumber(Exception):
    pass
class DuplicateAccountNumber(Exception):
    def __str__(self):
        return 'Account number already exists.'
class banker:
    def __init__(self,bank_data):
        self.bank_data=bank_data #testing purpose
        self.load_data()
    def load_data(self):
        try:
            with open('bank_data.json','r') as file:
                self.bank_data=json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):
            self.bank_data={}
    def save_data(self):
            with open('bank_data.json','w') as file:
                json.dump(self.bank_data,file,indent=4)
                  
    def add_customer(self,acc_choice,customer_name,opening_bal,gender,age):
        try:
        
            acc_choice=int(acc_choice)
            if acc_choice<=0:
                raise NegativeAccountNumber('Account number must be positive')
            if acc_choice in map(int,self.bank_data):
                raise DuplicateAccountNumber
            self.bank_data[acc_choice]={'Name':customer_name.lower(),'Balance':opening_bal,'Gender':gender,'Age':age}
            print(f'Customer {customer_name} added successfully.')
            self.save_data()
        except NegativeAccountNumber as err:
            print(err)
        except ValueError:
            print(f'Invalid Account number.')
        except DuplicateAccountNumber as err:
            print(err)
    def delete_customer(self, acc_choice):
        try:
            acc_choice = int(acc_choice)
            if acc_choice in self.bank_data:
                del self.bank_data[acc_choice]
                print(f'Customer with account number {acc_choice} deleted successfully.')
                self.save_data()
            else:
                print(f'Customer with account number {acc_choice} not found.')
        except ValueError:
            print(f'Invalid Account number.')
        except:
            print('Unexpected error occurred.')
    def view_customer(self):
        all_names=[sub_dict['Name'] for sub_dict in self.bank_data.values() if 'Name' in sub_dict]
        print(f'List of all customers:',all_names)
    def search_customer(self,customer_name):
        found_customer=[(number,sub_dict) for number,sub_dict in self.bank_data.items() if customer_name.lower() in sub_dict.values()]
        if found_customer:
            print(f'Search result:',found_customer)
        else:
            print('No such data exist.')
    def view_ll_customer(self):
        self.load_data()  # Load the latest data before printing
        print(f'Displaying all accounts:\n{self.bank_data}')
    def total_amount(self):
        total_amount=sum([sub_dict['Balance'] for numbre,sub_dict in self.bank_data.items() if 'Balance' in sub_dict])
        print(f'Total amount in the bank:{total_amount}')

if __name__=='__main__':   #for coder to testing purpose
    hdfc=banker(bd.BankData())
    hdfc.view_ll_customer()
    hdfc.add_customer(100, 'john', 2000, 'male', 30)
    hdfc.search_customer('abhi')
    hdfc.delete_customer(100)
    hdfc.view_ll_customer()
    hdfc.total_amount()
    
    
  


  
    