import json
class BankData:
    def __init__(self,filename='bank_data.json'):#optional filename
        self.file_name=filename
        self.data_acc=self.load_data() #loading initial data from a file.i.e. returns data from load_data

    def load_data(self):
        try:
            with open(self.file_name,'r') as file:
                data=json.load(file)
        except (FileNotFoundError,json.JSONDecodeError):## If the file doesn't exist or is not valid JSON, initialize with an empty dictionary
            data = { }
        return data
    def save_data(self):
        with open(self.file_name,'w') as file:
            json.dump(self.data_acc,file)
    def get_data_acc(self): 
        return self.data_acc
    
'''{
            101: {'Name': 'anjali', 'Balance': 2000, 'Gender': 'Female', 'Age': 40},
            102: {'Name': 'raj', 'Balance': 1000, 'Gender': 'Male', 'Age': 50},
            103: {'Name': 'abhishek', 'Balance': 2500, 'Gender': 'Male', 'Age': 20},
            104: {'Name': 'shivam', 'Balance': 3000, 'Gender': 'Male', "Age": 30}
        }'''
if __name__=='__main__':
    example_dict={
            101: {'Name': 'anjali', 'Balance': 2000, 'Gender': 'Female', 'Age': 40},
            102: {'Name': 'raj', 'Balance': 1000, 'Gender': 'Male', 'Age': 50},
            103: {'Name': 'abhishek', 'Balance': 2500, 'Gender': 'Male', 'Age': 20},
            104: {'Name': 'shivam', 'Balance': 3000, 'Gender': 'Male', "Age": 30}
        }
    BDObject=BankData('testing_BD.json')
    print(BDObject.get_data_acc())
    #BDObject.data_acc= example_dict.copy() can use this but..
    BDObject.get_data_acc().update(example_dict)
    BDObject.save_data()
    BDObject.load_data()
    BDObject.get_data_acc() #can type .data_acc
