import click
import random
import csv
from customer import *
from menu_items import *

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


class CustomerSystem(Singleton):
    def __init__(self, file_path, menu_items):
        self.file_path = file_path
        self.menu = menu_items
        self.customer_list = self.load_data()

    def load_data(self):
        # Loads customer data from a CSV file and returns a list of Customer objects
        customer_list = []
        try:
            with open(self.file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                for row in reader:
                    order_id = int(row[0])
                    customer_name = row[1]
                    phone_number = row[2]
                    menu_item_ids = []
                    for item_id in row[3:]:
                        if item_id.isdigit():
                            menu_item_ids.append(int(item_id))
                    menu_items = [self.get_menu_item_by_id(item_id) for item_id in menu_item_ids]
                    order = Order(order_id, customer_name, phone_number, menu_items)
                    customer = Customer(order_id, customer_name, phone_number, email="")  # Create a new Customer object
                    customer.order = order  # Assign the order to the customer
                    customer_list.append(customer)
        except FileNotFoundError:
            pass
        return customer_list

    
    def save_data(self):
        # Saves customer data to a CSV file
        with open(self.file_path, "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["order_id", "customer_name", "phone_number", "menu_item_ids"])
            for customer in self.customer_list:
                order = customer.order
                if order is not None:
                    menu_item_ids = [item.item_id for item in order.menu_items]
                    writer.writerow([order.order_id, customer.customer_name, customer.phone_number] + menu_item_ids)


    def generate_order_id(self):
        # Generates a unique order ID
        used_ids = [customer.order.order_id for customer in self.customer_list if customer.order is not None]
        order_id = random.randint(1, 9999)
        while order_id in used_ids:
            order_id = random.randint(1, 9999)
        return order_id

    def add_customer(self, customer_name, phone_number, order_items=None):
        # Adds a new customer to the system
        order_id = self.generate_order_id()
        order = None
        if order_items:
            order = Order(order_id, customer_name, phone_number, order_items)
        customer = Customer(order_id, customer_name, phone_number, email="")  # Create a new Customer object
        customer.order = order  # Assign the order to the customer
        self.customer_list.append(customer)
        self.save_data()


    def get_menu_item_by_id(self, item_id):
        # Returns a menu item object based on the provided item ID
        for menu_item in self.menu:
            if menu_item.item_id == item_id:
                return menu_item
        return None

    def place_order(self):
        # Allows a customer to place an order
        order_id = self.generate_order_id()
        customer = self.get_customer_by_id(order_id)
        MenuItem.display_menu(self.menu)

        customer_name = click.prompt("\nEnter your name", type=str)
        while not customer_name.isalpha():
            click.echo("Invalid name. Please enter a valid name.")
            customer_name = click.prompt("Enter your name", type=str)

        phone_number = click.prompt("Enter your phone number", type=str)
        while not phone_number.isdigit() or len(phone_number) != 10:
            click.echo("Invalid phone number. Please enter a 10-digit phone number.")
            phone_number = click.prompt("Enter your phone number", type=str)

        if customer is None:
            item_ids = click.prompt(
                "Enter menu item IDs to place an order (comma-separated) or 0 to end the order",
                type=str
            )
            item_ids = item_ids.strip().split(",")
            menu_items = []
            total_price = 0

            for item_id in item_ids:
                if item_id == "0":
                    click.echo("Order cancelled.\nBYE")
                    return None

                while not item_id.isdigit():
                    click.echo("Invalid menu item ID. Please enter a valid menu item ID.")
                    item_id = click.prompt(
                        "Enter menu item IDs to place an order (comma-separated) or 0 to end the order",
                        type=str
                    )

                menu_item = self.get_menu_item_by_id(int(item_id))
                if menu_item is not None:
                    menu_items.append(menu_item)
                    total_price += menu_item.price
                else:
                    click.echo(f"Invalid menu item ID: {item_id}. Please try again.")

            click.echo("******************************")
            click.echo(f"Hi {customer_name}")
            click.echo("Here is your Order details:\n")
            click.echo(f"Order ID: {order_id}")
            click.echo("Menu items:")
            for item in menu_items:
                click.echo(f"- {item.name} (${item.price})")
            click.echo(f"Total price: ${total_price:.2f}")

            order = Order(order_id, customer_name, phone_number, menu_items)
            customer = Customer(order_id, customer_name, phone_number,email="")  # Create a new Customer object
            customer.order = order  # Assign the order to the customer
            self.customer_list.append(customer)
            self.save_data()
            click.echo("\nOrder placed successfully.")
        else:
            click.echo("Unable to place the order. Customer not found.")

    def get_customer_by_id(self, order_id):
        # Returns a customer object based on the provided order ID
        for customer in self.customer_list:
            if customer.order_id == order_id:
                return customer
        return None



class SingletonOrderSystem(CustomerSystem):
    pass


if __name__ == "__main__":
    file_path = "customers.csv"
    menu_items = MenuItem.load_from_csv('menu_items.csv')
    order_system = SingletonOrderSystem(file_path, menu_items)
    order_system.place_order()
