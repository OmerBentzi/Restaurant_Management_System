from click_params import EMAIL
import csv
import os
from menu_items import *
from order import *
from table import *
from customer import *



#this class it to show the Employee system backend the user can't see this
class Employee:
    def __init__(self, employee_id: int, name: str, email, phone: int, role: str, permission: str,table_number = None):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role
        self.permission = permission
        self.table_number = table_number
        self.employee_list = []

    # Add the employee
    def add_employee(self, employee):
        self.employee_list.append(employee)


    # If  needed to edit an employee 
    def edit_employee(self, employee_id, name, email, phone, role, permission):
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                employee.name = name
                employee.email = email
                employee.phone = phone
                employee.role = role
                employee.permission = permission
                break
        else:
            # If the employee cant be found by it's ID
            raise ValueError(f"Employee with id {employee_id} does not exist")

    # If needed to delete the employee
    def delete_employee(self, employee_id):
        for index, employee in enumerate(self.employee_list):
            if employee.employee_id == employee_id:
                del self.employee_list[index]
                break
        else:
            # If the employeecant be found by the id
            raise ValueError(f"Employee with id {employee_id} does not exist")


    # Using the employee ID we can assign a table to him 
    def assign_table(self, table, employee_id):
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                table.assign_employee(employee)
                break
        else:
            #Wont let us assign employee if he dosn't exist
            raise ValueError(f"Employee with id {employee_id} does not exist")

    # Using the eq function to compare for equality
    def __eq__(self, other):
        if isinstance(other, Employee):
            return (
                self.employee_id == other.employee_id
                and self.name == other.name
                and self.email == other.email
                and self.phone == other.phone
                and self.role == other.role
                and self.permission == other.permission
            )
        return False


# This class if for the manager wo can only access by password and can edit the employee
class Manager(Employee):
    def __init__(self, employee_id, name, email, phone):
        super().__init__(employee_id, name, email, phone,'Manager', 'All Access')

    def add_employee(self, employee):
        employee.permission = 'Limited Access'
        super().add_employee(employee)


# Saving all the employees data under this class 
class EmployeeData:
    def __init__(self, file):
        self.file = file
        self.file_path = self.file
        self.employee_list = self.load_data()

    # Searching if there's a csv already made and if yes shows us all the employee details
    def read_data(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            employee_list = []
            for row in reader:
                employee_id, name, email, phone, role, permission,table_number = row
                employee = Employee(int(employee_id), name, email, phone, role, permission,table_number)
                employee_list.append(employee)
        return employee_list

    # This is mainly for the manager class to edit the employees and the permission
    def write_data(self, employee_list, table_number= None):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['employee_id', 'name', 'email', 'phone', 'role', 'permission', 'table_numbers'])
            for employee in employee_list:
                writer.writerow([employee.employee_id,employee.name,employee.email,employee.phone,employee.role,employee.permission,table_number])

    # Saving the changed data into the csv file
    def save_data(self, employee_list, table_number= None):
        self.write_data(employee_list,table_number)


    # Loading the csv file 
    def load_data(self):
        self.employee_list = self.read_data()
        return self.employee_list

