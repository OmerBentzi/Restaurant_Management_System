import csv
import os
from order import *

# Customer class
class Customer:
    def __init__(self, order_id, customer_name, phone_number, email):
        self.order_id = order_id
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.email = email
        self.orders = []

    def place_order(self, order):
    
        # Adds a new order to the customer's list of orders.
        
        self.orders.append(order)
        return True

    def modify_order(self, order_id, new_items):
        
       # Modifies the menu items of a specific order.
        
        for order in self.orders:
            if order.order_id == order_id:
                order.menu_items = new_items
                return True
        return False

    def cancel_order(self, order):
        
       # Cancels a specific order from the customer's list of orders.
        
        if order in self.orders:
            self.orders.remove(order)
            return True
        return False


class DataCustomer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.customer_list = []

    def read_data(self):
        
      #  Reads customer data from a CSV file and returns a list of Customer objects.
        
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            customer_list = []
            for row in reader:
                order_id, customer_name, phone_number, email = row
                customer = Customer(int(order_id), customer_name, phone_number, email)
                customer_list.append(customer)
        return customer_list

    def write_data(self, customer_list):
        
       # Writes customer data to a CSV file.
        
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['order_id', 'customer_name', 'phone_number', 'email'])
            for customer in customer_list:
                writer.writerow([customer.order_id, customer.customer_name, customer.phone_number, customer.email])

    def save_data(self):
        
     #  Saves the current customer data to the CSV file.
        
        self.write_data(self.customer_list)

    def load_data(self):

      #  Loads customer data from the CSV file and returns the list of Customer objects.
        
        self.customer_list = self.read_data()
        return self.customer_list
