
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
employee=SHEET.worksheet('employee')

data_employee=employee.get_all_values()


class Employee:
 def __init__(self, id_nr, name, age, country):
        self.id_nr=id_nr
        self.name=name
        self.age=age
        self.country=country
        
 def data_output(self):
    return f"You have added --- Employe-id: {self.id_nr} ---- Name: {self.name} --- Age: {self.age} --- Country: {self.country}"


e1=Employee(333, 'Eric anderrson', 27, 'sweden')
print(e1.data_output())