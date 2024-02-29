import customer_module as cm
import banker_module as bm
import bank_data as bd
import json 
example_dict = {
    101: {'Name': 'anjali', 'Balance': 2000, 'Gender': 'Female', 'Age': 40},
    102: {'Name': 'raj', 'Balance': 1000, 'Gender': 'Male', 'Age': 50},
    103: {'Name': 'abhishek', 'Balance': 2500, 'Gender': 'Male', 'Age': 20},
    104: {'Name': 'akshay', 'Balance': 3000, 'Gender': 'Male', 'Age': 18}
}
'''
->JSON (JavaScript Object Notation) is a 
lightweight data interchange format 
that is easy for humans to read and write, 
and easy for machines to parse and generate.
->Parsing refers to the process of 
extracting information from a data structure,
 and generating means creating data structures.
'''

#Write a program to demonstrate the bank management Console based application.

welcome_line='WELCOME TO PYTHON BANK MANAGEMENT SYSTEM'

#Displaying welcome line exactly in center with asterisk on both side
'''terminal_width=108

dash_count=(108-len(welcome_line))//2

centered_text='*'*dash_count+welcome_line+'*'*dash_count
print(centered_text)'''

def beginning():
    print(welcome_line.center(108)) #terminal width is 108 obtained using shutil module.

    role_msg='Select your role.'
    select1='1)Banker'
    select2='2)Customer'
    select3='3)Exit'

    print(role_msg.center(108))
    print(select1.center(108))
    print(select2.center(108))
    print(select3.center(108))

def operations_menu_banker():
    print("Welcome to banker's App:")
    print("Operations Menu.\n".center(108))
    print('1) Add Customer.'.center(108))
    print('2) View Customer.'.center(108))
    print('3) Search Customer.'.center(108))
    print('4) View all Customer.'.center(108))
    print('5) Total amounts in bank.'.center(108))

def operations_menu_customer():
    print("Welcome to customer's App:")
    print("Operations Menu.\n".center(108))
    print('1)Withdraw amount.'.center(108))
    print('2)deposit amount.'.center(108))
    print('3)view balance.'.center(108))

def main():
    bank_data=bd.BankData()
    bank_data.data_acc.update(example_dict)
    bank_data.save_data() 
    while True: 
        try:
            input_choice=int(input('Enter your Role:'))
        except ValueError:
            print('Enter a valid integer')
            continue
        
        if input_choice==1: #banker role
                bank_manager=bm.banker(bank_data) #object of banker class
                operations_menu_banker()
                try:
                    operations_choice=int(input('Enter operation which you want to perform:'))
                    if operations_choice==1:#adding account
                        while operations_choice:
                            acc_choice=int(input('Enter your account number:'))
                            customer_name=input('enter customer name:')
                            opening_bal=int(input('Enter opening balance:'))
                            gender=input('Enter the gender:')
                            age=int(input('Enter the age:'))
                        
                            bank_manager.add_customer(acc_choice,customer_name,opening_bal,gender,age)

                            next_operation=input('Do you want to perform more operations? press "y" for yes and press "n" for no:')
                            if next_operation.lower()=='n':
                                break
                    elif operations_choice==2: #view  customers name:-> showing list of all customersname
                        bank_manager.view_customer()
                    elif operations_choice==3: #search customer
                        customer_name=input('Enter the customer name:').lower()
                        bank_manager.search_customer(customer_name)
                    elif operations_choice==4: #all details of customers
                        bank_manager.view_ll_customer()
                    elif operations_choice==5: #total amount in bank
                        bank_manager.total_amount()
                    else:
                        pass
                except ValueError:
                    print('enter a valid choice')
                    continue
        elif input_choice==2:#customer role
                bank_customer=cm.customer(bank_data)
                operations_menu_customer()
                try:
                    operations_choice=int(input('Enter operation which you want to perform:'))
                    if operations_choice==1: #widhdraw amount
                        acc_number=int(input('enter your account number:'))
                        withdraw=int(input('Enter the withdrawl amount:'))
                        bank_customer.withdraw_amount(acc_number,withdraw)
                    elif operations_choice==2: #deposit amount
                        acc_number=int(input('Enter the account number:'))
                        deposit=int(input("Enter the deposit amount:"))
                        bank_customer.deposit_amount(acc_number,deposit)
                    elif operations_choice==3: #view balance
                        acc_number=int(input('Enter the account number:'))
                        bank_customer.view_balance(acc_number)
                    else:
                        pass
                except ValueError:
                    print('enter a valid choice')

        elif input_choice==3: #exists
            return print('Have a good day!')
        else:
            pass

beginning()
main()