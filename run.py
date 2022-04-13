""" Import library from google to use as api. Code from Code institute"""
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

# My own code starts here.


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
        output_msg = (f"Your input: -- Employee-id:"
                      f"{self.id_nr} -- Salary:{self.salary}"
                      f" -- Name: {self.name} -- Country: {self.country} --")
        return output_msg


e1 = Employee(0, "", 0, "")  # Provide default values.


def update(data):
    """Acess the row called employee in googlespreadsheet,
     and append the data"""
    add_employee = SHEET.worksheet("employee")
    add_employee.append_row(data)


empty_list = []  # empty list to put spreadsheet data in


def add_input_spreadsheet():
    """Ask the user for input to put in the object variable,
    append the data inside empty list if the wrong input is,
    provided break the loop if values below 0 is inputted break the loop"""
    num_one = 1
    for i in range(0, num_one):
        try:
            e1.id_nr = int(input("Add an Employee ID,only"
                                 " numbers above 0 is allowed:\n"))
            if e1.id_nr < 0:
                print("------------------------------------")
                print("Please type a value above 0")
                print("------------------------------------")
                print("WARNING..failed to add employee")
                print("------------------------------------")
                break
            if e1.id_nr > 0:
                detect_values(e1.id_nr)
                print("WARNING...if 0 is pressed employee will not"
                      " be added to the system.\n")
                answer = int(input("Press 0 to cancel and exit,"
                                   "or press any other number to continue:\n"))
                if answer == 0:
                    break
                else:
                    print("------------------------------------")
                    e1.salary = int(input("Add a Salary per month in Us"
                                          " dollars, only numbers above"
                                          " 0 is allowed:\n"))
                    print("------------------------------------")
            if e1.salary < 0:
                print("Please type a value above 0\n")
                print("WARNING..failed to add employee\n")
                break
            e1.name = input("Add a Name:\n")
            e1.country = input("Add a Country:\n")
            empty_list.append(e1.id_nr)
            empty_list.append(e1.salary)
            empty_list.append(e1.name)
            empty_list.append(e1.country)
            break
        except:
            print("Only one value and only one number is allowed")
            print("WARNING...Failed to add employee,please"
                  " try again with the right values.")


def request_data():
    """Retrive data from googlespreedsheet and output the requested data,
    that has been inputed from the user"""
    values = SHEET.worksheet('employee').get_all_values()
    employee_number = 0
    for value in values[1:]:
        employee_number += 1  # increment the employee number and print it out
        print(f"-------------------------Employee:{employee_number}"
              f"-----------------------------")
        print("--------------------------------------------------------------")
        show_msg = (f" Employee ID : {value [0]}"
                    f" : Salary : {value[1]}"
                    f" : Name : {value[2]}"
                    f" : Country : {value[3]} :")
        print(show_msg)
        print("--------------------------------------------------------------")


def detect_values(id_validate):
    """ Function that looks in the googlespreadsheet aftet the row,
        "Employee-id, checks all the values and compares it with
         the input to display a message if a value exist or not
    """
    values = SHEET.worksheet('employee').get_all_values()
    find_id = []
    for value in values[1:]:
        detect_id = int(value[0])
        find_id.append(detect_id)
    if id_validate in find_id:
        print("------------------------------------")
        print("WARNING...The employee-Id-you provided alredy exist")
        print("------------------------------------")
    else:
        print("------------------------------------")
        print("The employee-id is avalible")
        print("------------------------------------")


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
        for value in values[1:]:
            new = int(value[1])
            salary_info.append(new)
            sum_salary = sum(salary_info)
    print("-----------------------------------------------------")
    print(f"The total salary cost is: {sum_salary} $ Dollars per month.")
    print("-----------------------------------------------------")


def main():
    """Main menu where user can choose what function to run with a number,
    All functions runs from this function, the menu loops untill 0 is pressed,
    and the loop stops after user have added employee to googlesheet"""

    menu_choice = None
    while menu_choice != 0:
        try:
            if menu_choice == 1:
                add_input_spreadsheet()
                add_data = [str(num) for num in empty_list]
                update(add_data)
                print(e1.data_output())
                break
            elif menu_choice == 2:
                request_data()
                print("------------------------------------")
                input("Press any key to get back to the Employee main menu\n")
                print("------------------------------------")
            elif menu_choice == 3:
                calculate_salary()
                print("------------------------------------")
                input("Press any key to get back to the Employee main menu\n")
                print("------------------------------------")
            print("Welcome to Employee adder, type a number and press enter.")
            print("------------------------------------")
            print("1. Add employee")
            print("2. Show added employee")
            print("3. Caluclate salary of the employees")
            print("0. Exit menu")
            print("------------------------------------")
            menu_choice = int(input())
        except:
            print("------------------------------------")
            print("Please type a number between 1 to 3 in the main",
                  " menu or type 0 to exit.")
            input("Press any key to get back to the last menu\n")
            print("------------------------------------")


if __name__ == '__main__':
    main()  # All the functions are called from this function
    print("Employee adder will now shutdown....")
