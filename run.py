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
       declare the variables use the attributes for input later.
    """
    def __init__(self, id_nr, name, salary, country):
        self.id_nr = id_nr
        self.name = name
        self.salary = salary
        self.country = country

    def data_output(self):
        """ Output and display message when the user have added
            the input into the class variables and returning all
            the inputed values.
        """
        print("Loading................")
        output_msg = (f"Your input: -- Employee-id:"
                      f"{self.id_nr} -- Salary:{self.salary}"
                      f" -- Name: {self.name} -- Country: {self.country} --")
        return output_msg


e1 = Employee(0, "", 0, "")  # Provide default values.


def update(data):
    """Acess the row called employee in googlespreadsheet,
     and append the data into the function called"""
    add_employee = SHEET.worksheet("employee")
    add_employee.append_row(data)


empty_list = []  # empty list to put spreadsheet data in


def add_input_spreadsheet():
    """Ask the user for input if the value is below zero for employee-id input
       and below 0 for salary input then a message will show up
       to break the loopand display a message telling the
       user that it failed to add input. If anything
       than a whole number is inputed in the employe and salary input
       by the user an exepection will occur and display a message
       telling the user to
       put in the right values.

       The input data from the user will be appended to a empty list
       called empty_list.
       If the values in Employee id alredy exist in the
       googlespreadsheet a message.
       will display informing the user that the value
       alredy exist,if the value does
       not exist a message will display and telling
       the user that the value is available.
       """
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
        except ValueError:
            print("Only one whole number is allowed, example: 2,3,4,5")
            print("WARNING...Failed to add employee,please"
                  " try again with the right values.")


def request_data():
    """Retrive data from googlespreedsheet, in a foor loop.
       jump over the first row in the list to not display
       with the value [1: in the loop]. Increment the employee
       _number everytime an employee has been added to the list.
       Display in a strin literal all the values that has been,
       added to the google spreadsheet.
       and put the data in to varible called """
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
    """ Function that one argument and takes value
        from the googlespreadsheet
        in the "emloyee-id" row, takes that value and appends it
        in a list called find_id. Checks if the input argument
        matches with the value inside employee-id row, if the value
        exist then print a warning message informing the user
        that the value exist. if the value does not exist
        then inform the user that the value dont exist.

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
    """Retrive the row called salary in the googlespreadsheet
    with the variable "values". If the salary is empty in the
    spreadsheet, then display message showing that the total
    cost is "0". Append the values variable inside a empty list.
     convert the values to integers and use method called "sum"
     to sum the values inside the list. After the caluclation
     has been executed display the total cost in a string literal."""
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
    and the loop stops after user have added
    employee to googlesheet,if user inputs
    value below "0" a message will display or
    if a user inputs anything other than
    a whole number."""

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
            if menu_choice < 0:
                print("please type a number above 0\n")
                input("Press any key to get back to the Employee main menu\n")
        except ValueError:
            print("------------------------------------")
            print("Please type a number between 1 to 3 in the main",
                  " menu or type 0 to exit.")
            input("Press any key to get back to the last menu\n")
            print("------------------------------------")


if __name__ == '__main__':
    main()  # All the functions are called from this function
    print("Employee adder will now shutdown....")
