import click
import sys
from customer import *
from employee import *
from menu_items import *
from menu import *
from order import *
from table import *
from customer_system import *
from employee_system import *

class RestaurantFacade:
    def __init__(self):
        self.menu_items = MenuItem.load_from_csv('menu_items.csv')
        self.customer_system = CustomerSystem('customer_data.csv', self.menu_items)
        self.employee_system = EmployeeSystem('employee_data.csv')
        self.order_system = CustomerSystem('customer_orders.csv', self.menu_items)

    def display_main_menu(self):
        while True:
            click.echo("\nMain Menu")
            click.echo("1. Customer")
            click.echo("2. Employee")
            click.echo("0. Exit")

            choice = click.prompt("Enter your choice", type=int)

            if choice == 1:
                self.customer_menu()
            elif choice == 2:
                self.employee_menu()
            elif choice == 0:
                self.exit()
            else:
                click.echo("Invalid choice. Please try again.")

    def customer_menu(self):        
        while True:
            click.echo("\nCustomer Menu")
            click.echo("1. Place Order")
            click.echo("2. Exit")

            choice = click.prompt("Enter your choice", type=int)

            if choice == 1:
                self.order_system.place_order()
            elif choice == 2:
                break
            else:
                click.echo("Invalid choice. Please try again.")

    def employee_menu(self):
        self.employee_system.employee_menu(self.menu_items,self.order_system)

    def exit(self):
        click.echo("\nGoodbye maybe next time.\n")
        sys.exit()

if __name__ == "__main__":
    facade = RestaurantFacade()
    facade.display_main_menu()
