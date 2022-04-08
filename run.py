""" Import library from google to use as api."""
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
    """Create a class with attributes of an object and,
       declare the variables use the attributes for input later
    """
    def __init__(self, id_nr, name, salary, country):
        self.id_nr = id_nr
        self.name = name
        self.salary = salary
        self.country = country

    def data_output(self):
        """ Output the asked info into the attriute variables,
         and display the message"""
        print("loading................")
        print("Employe have been successfully added to the database")
        output_msg = (f"You have added --- Employe-id:"
                      f"{self.id_nr} ---- Salary:{self.salary}"
                      f"--- Name: {self.name} --- Country: {self.country}")
        return output_msg


e1 = Employee(0, "", 0, "")  # initilazie object and give empty values


def update(data):
    """Acess the row called employee in googlespreadsheet,
     and append the data"""
    add_employee = SHEET.worksheet("employee")
    add_employee.append_row(data)


empty = []  # empty array to put spreadsheet data in

num_one = 1  # variable for index


def add_input_spreadsheet():
    """Ask the user for input to put in the object variable,
    append the data inside empty list"""
    for i in range(0, num_one):

        e1.id_nr = int(input('add an Employee ID:'))
        e1.salary = input('add a Salary in Us dollar:')
        e1.name = input('add a Name:')
        e1.country = input('add a Country:')

    empty.append(e1.id_nr)
    empty.append(e1.salary)
    empty.append(e1.name)
    empty.append(e1.country)


def request_data():
    """Retrive data from googlespreedsheet and output the requested data,
    that has been inputed from the user"""
    values = SHEET.worksheet('employee').get_all_values()

    for x in values:

        print("--------------------------------------------------------------")
        print(f" Employee ID:{x [0]}.Salary:{x[1]}.Name:{x[2]}.Country:{x[3]}")
        print("--------------------------------------------------------------")


def calculate_salary():
    """Reterive salary data inputed from the user and append the data,
    inside an empty list. Use sum method to calculate the sum in the list,
    and show the sum result"""
    values = SHEET.worksheet('employee').get_all_values()
    salary_info = []
    for x in values[1:]:
        new = int(x[1])
        salary_info.append(new)
        sum_salary = sum(salary_info)
    print(f"The total sum of the salaries are: {sum_salary} $Dollar")


def validate_data(data):
    try:
        e1.id_nr = input()
    except:
        print("you need to print a number")


def main():
    """Main menu where user can chose wich function to run with a number,
    All functions runs from this function"""
    if menu_choice == 1:
        add_input_spreadsheet()
        sales_data = [str(num) for num in empty]
        update(sales_data)
        print(e1.data_output())
    if menu_choice == 2:
        request_data()
    if menu_choice == 3:
        calculate_salary()


menu_choice = None
while menu_choice != 0:
    print("Choose one of the options ")
    print("1. Add employee to database")
    print("2. Show employee from the database")
    print("3. Caluclate salary of the employees")
    print("0. to exit this menu")
    menu_choice = int(input())
    main()

