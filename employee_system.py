import click
from employee import *
from customer_system import *
from table import *
from menu_items import *

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


class EmployeeSystem(EmployeeData, Singleton):
    def __init__(self, file_path):
        EmployeeData.__init__(self, file_path)
        self.employee_list = self.load_data()
        self.table_list = self.load_data()
        self.is_manager = False

    def authenticate_manager(self):
        # Authenticates the manager by checking the entered password
        if not self.is_manager:
            password = click.prompt("Enter manager password", hide_input=False, type=str)
            if password == "password":
                self.is_manager = True
                return True
            else:
                click.echo("Invalid password. Access denied.")
                return False
        return True

    def get_employee_by_id(self, employee_id):
        # Returns an employee object based on the provided employee ID
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                return employee
        return None

    def add_employee(self):
        # Adds a new employee to the system after collecting necessary information from the manager
        if not self.authenticate_manager():
            click.echo("Access denied. Only the manager can add employees.")
            return

        employee_id = click.prompt("Enter employee ID", type=str)
        while not employee_id.isdigit():
            click.echo("Invalid ID. Please enter a correct ID.")
            employee_id = click.prompt("Enter employee ID", type=str)

        name = click.prompt("Enter employee name", type=str)
        while not name.isalpha():
            click.echo("Invalid name. Please enter a valid name.")
            name = click.prompt("Enter employee name", type=str)

        email = click.prompt("Enter employee email", type=str)

        phone = click.prompt("Enter employee phone", type=str)
        while not phone.isdigit() or len(phone) != 10:
            click.echo("Invalid phone number. Please enter a 10-digit phone number.")
            phone = click.prompt("Enter employee phone", type=str)

        role = click.prompt("Enter employee role", type=str)
        while not role.isalpha() or role.lower() not in ["chef", 'waiter']:
            click.echo("Invalid role. waiter or chef.")
            role = click.prompt("Enter employee role", type=str)

        permission = click.prompt("Enter permission", type=str)
        while not permission.isalpha() or permission.lower() not in ["kitchen", 'Tables', "all"]:
            click.echo("Invalid permission. kitchen, Tables, all.")
            permission = click.prompt("Enter employee permission", type=str)

        employee = Employee(employee_id, name, email, phone, role, permission)

        self.employee_list.append(employee)
        self.save_data(self.employee_list)
        click.echo("Employee added successfully.")

    def edit_employee(self):
        # Edits the details of an existing employee
        if not self.authenticate_manager():
            click.echo("Access denied. Only the manager can edit employees.")
            return

        employee_id = click.prompt("Enter employee ID", type=str)
        employee = self.get_employee_by_id(employee_id)
        if employee is not None:
            name = click.prompt("Enter an updated employee name", type=str)
            while not name.isalpha():
                click.echo("Invalid name. Please enter a valid name.")
                name = click.prompt("Enter employee name", type=str)

            email = click.prompt("Enter employee email", type=str)

            phone = click.prompt("Enter new employee phone", type=str)
            while not phone.isdigit() or len(phone) != 10:
                click.echo("Invalid phone number. Please enter a 10-digit phone number.")
                phone = click.prompt("Enter employee phone", type=str)

            role = click.prompt("Enter employee role", type=str)

            employee.name = name
            employee.email = email
            employee.phone = phone
            employee.role = role

            self.save_data(self.employee_list)
            click.echo("Employee edited successfully.")
        else:
            click.echo(f"Employee with ID {employee_id} not found.")

    def delete_employee(self):
        # Deletes an employee from the system
        if not self.authenticate_manager():
            click.echo("Access denied. Only the manager can delete employees.")
            return
        employee_id = click.prompt("Enter employee ID to delete", type=str)
        employees_to_delete = []
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                employees_to_delete.append(employee)

        if employees_to_delete:
            for employee in employees_to_delete:
                self.employee_list.remove(employee)
            self.save_data(self.employee_list)
            click.echo("Employee(s) deleted successfully.")
        else:
            click.echo(f"Employee with ID {employee_id} not found.")

    def assign_table(self):
        # Assigns a table to an employee
        table_number = click.prompt("Enter table number to assign", type=str)
        employee_id = click.prompt("Enter employee ID to assign", type=str)
        table = self.get_table_by_number(table_number)
        if table is not None:
            table.assign_employee(employee_id)
            self.save_data(self.employee_list, self.table_list)
            click.echo(f"Table with number {table_number} not found.")
        else:
            click.echo(f"Table {table_number} assigned to employee with ID {employee_id} successfully.")

    def get_table_by_number(self, table_number):
        # Returns a table object based on the provided table number
        for table in self.table_list:
            if table.table_number == table_number:
                return table
        return None

    def employee_menu(self, menu_items, order_system):
        # Displays a menu for the employee to perform various operations
        while True:
            click.echo("\n===== Employee Menu =====\n")
            click.echo("1. Add Employee")
            click.echo("2. Edit Employee")
            click.echo("3. Delete Employee")
            click.echo("4. Assign Table")
            click.echo("5. Place Order")
            click.echo("6. Exit")

            choice = click.prompt("\nEnter your choice")
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.edit_employee()
            elif choice == "3":
                self.delete_employee()
            elif choice == "4":
                self.assign_table()
            elif choice == "5":
                order_system.place_order()
            elif choice == "6":
                click.echo("\nExiting\n")
                break
            else:
                click.echo("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu_items = []
    system = EmployeeSystem("employee_data.csv")
    order_system = CustomerSystem('customer_orders.csv', menu_items)
    system.employee_menu(menu_items, order_system)
