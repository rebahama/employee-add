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


class Employee:
    def __init__(self, id_nr, name, salary, country):
        self.id_nr = id_nr
        self.name = name
        self.salary = salary
        self.country = country

    def data_output(self):
        print("loading................")
        print("Employe have been successfully added to the database")
        return f"You have added --- Employe-id: {self.id_nr} ---- Salary: {self.salary}\--- Name: {self.name} --- Country: {self.country}"


e1 = Employee(0, "", 0, "")


def update(data):
    add_employee = SHEET.worksheet("employee")
    add_employee.append_row(data)


empty = []

n1 = 1


def add_input_spreadsheet():

    for i in range(0, n1):

        e1.id_nr = int(input('add an Employee ID:'))
        e1.salary = input('add a Salary in Us dollar:')
        e1.name = input('add a Name:')
        e1.country = input('add a Country:')

    empty.append(e1.id_nr)
    empty.append(e1.salary)
    empty.append(e1.name)
    empty.append(e1.country)


def request_data():
    values = SHEET.worksheet('employee').get_all_values()

    for x in values:

        print("----------------------------------------------------------------------")
        print(f"  Employee ID:{x [0]}:    Salary:{x[1]}:   Name: {x[2]}: Country:{x[3]}")
        print("----------------------------------------------------------------------")


def add_data(data):
    values = SHEET.worksheet('employee').get_all_values()
    value = SHEET.worksheet('employee').get_all_values()[0]
    total = 0
    for x in values[1:]:
            new = int(x[1])
            neeeew = new+100
            print(neeeew)


def validate_data(data):
    try:
        e1.id_nr = input()
    except:
        print("you need to print a number")


def main():
    if menu_choice == 1:
        add_input_spreadsheet()
        sales_data = [str(num) for num in empty]
        update(sales_data)
        print(e1.data_output())
    if menu_choice == 2:
        request_data()
add_data(2)

menu_choice = None
while menu_choice != 0:
    print("Choose one of the options ")
    print("1.Add employee to database")
    print("2.Show employee from the database")
    print("3. Caluclate salary of the employees")
    print("0 to exit this menu")
    menu_choice = int(input())
    main()
 
