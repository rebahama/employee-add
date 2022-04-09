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
        print("Loading................")
        print("Employee have been successfully added to the database.")
        output_msg = (f"You have added -- Employe-id:"
                      f"{self.id_nr} -- Salary:{self.salary}"
                      f" -- Name: {self.name} -- Country: {self.country} --1"
                      f"\nEmployee adder will now exit.....")
        return output_msg


e1 = Employee(0, "", 0, "")  # initilazie object and give empty values


def update(data):
    """Acess the row called employee in googlespreadsheet,
     and append the data"""
    add_employee = SHEET.worksheet("employee")
    add_employee.append_row(data)


empty = []  # empty list to put spreadsheet data in

num_one = 1  # variable for index


def add_input_spreadsheet():
    """Ask the user for input to put in the object variable,
    append the data inside empty list"""
    for i in range(0, num_one):

        e1.id_nr = int(input('Add an Employee ID:\n'))
        e1.salary = input('Add a Salary in Us dollar:\n')
        e1.name = input('Add a Name:\n')
        e1.country = input('Add a Country:\n')

    empty.append(e1.id_nr)
    empty.append(e1.salary)
    empty.append(e1.name)
    empty.append(e1.country)


def request_data():
    """Retrive data from googlespreedsheet and output the requested data,
    that has been inputed from the user"""
    values = SHEET.worksheet('employee').get_all_values()

    for x in values[1:]:

        print("--------------------------------------------------------------")
        show_msg = (f" Employee ID 2 : {x [0]}"
                    f" : Salary : {x[1]}"
                    f" : Name : {x[2]}"
                    f" : Country : {x[3]} :")
        print(show_msg)
        print("--------------------------------------------------------------")


def calculate_salary():
    """Reterive salary data inputed from the user and append the data,
    inside an empty list. Use sum method to calculate the sum in the list,
    and show the sum result"""
    values = SHEET.worksheet('employee').get_all_values()
    sum_salary = "0"
    if sum_salary == "":
        print("None")
    else:
        salary_info = []
        for x in values[1:]:
            new = int(x[1])
            salary_info.append(new)
            sum_salary = sum(salary_info)

    print(f"The salary cost is: {sum_salary} $ Dollars per month")


def validate_data(data):
    try:
        e1.id_nr = input()
    except:
        print("you need to print a number")


def main():
    """Main menu where user can choose wich function to run with a number,
    All functions runs from this function, the menu loops untill 0 is pressed,
    and the loop stops after user have added employer to googlesheet"""

    menu_choice = None
    while menu_choice != 0:
        if menu_choice == 1:
            add_input_spreadsheet()
            add_data = [str(num) for num in empty]
            update(add_data)
            print(e1.data_output())
            break
        elif menu_choice == 2:
            request_data()
        elif menu_choice == 3:
            calculate_salary()
        print("------------------------------------")
        print("Welcome to Employee adder, please choose a number")
        print("1. Add employee")
        print("2. Show added employee")
        print("3. Caluclate salary of the employees")
        print("0. Exit menu")
        print("------------------------------------")
        menu_choice = int(input())


main()
