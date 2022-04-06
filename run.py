
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Import library from google to use as api.
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# store the api in variable 
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('employee-add')
# acess spreadsheet data
employee = SHEET.worksheet('employee')


data_employee = employee.get_all_values()
print(data_employee)


class Employee:
    def __init__(self, id_nr, name, age, country):
        self.id_nr = id_nr
        self.name = name
        self.age = age
        self.country = country
        
    def add_input(self):
   
        self.id_nr = int(input('write employ nr please'))
        self.name = (input('write name please'))
        self.age = int(input('write age please'))
        self.country = (input('write country please'))

    def data_output(self):
        return f"You have added --- Employe-id: {self.id_nr} ---- Name: {self.name} --- Age: {self.age} --- Country: {self.country} to the employee database"

    
e1=Employee(0, "", 0, "")

def update(data):
 
 add_employee=SHEET.worksheet("employee")
 add_employee.append_row(data)



#def add_numbers():
#num1=input('add a word')

empty=[]


def add_data_spreadsheet():
 n1=1
 for i in range(0, n1):
    e1.id_nr=input('add an Employee ID')
    e1.name=input('add a name')
    e1.age=input('add a age')
    e1.country=input('add a country')
    
   
    empty.append(e1.id_nr)
    empty.append(e1.name)
    empty.append(e1.age)
    empty.append(e1.country)
    
add_data_spreadsheet()

sales_data=[str(num) for num in empty]

update(sales_data)
print(e1.data_output())
print(empty)





#e1.add_input()
#print(e1.data_output())




